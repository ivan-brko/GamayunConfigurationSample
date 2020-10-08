# Sample configuration for Gamayun
This repo contains a minimal sample configuration for [Gamayun Data collector tool](https://github.com/ivan-brko/Gamayun), and it can/should be used as a base for creation of new configuration.

# Contents

* [Docker](#docker-top)
  * [Running on Raspberry PI (arm64v8)](#rpi)
  * [For people unfamiliar with Docker](#for-docker-unfamiliar)
    * [docker](#docker-low)
    * [docker-compose](#docker-compose)
* [Python scripts](#python-scripts)
* [Sample jobs](#sample-jobs)

<a name="docker-top"></a>
# Docker
While Gamayun can be run locally, it is easiest to run it with Docker and this repository contains all the needed docker files.

Gamayun docker image is used as a base for an image which contains this configuration and docker-compose is setup to run Gamayun (with this configuration) and MongoDB and to connect them. 

To run all of this, position your terminal in the root of this directory and run:
```docker
docker-compose -f docker-compose.yml up
```
If any other packages are missing that need to be used just add a line that installs that package for Alpine (or maybe for pip) in the dockerfile.

<a name="rpi"></a>
## Running images on Raspberry PI
If you want to run on Raspberry PI (on some other arm64v8 architecture), there are prebuild docker images for that as well:
```docker
docker-compose -f arm64v8.docker-compose.yml up
```

<a name="for-docker-unfamiliar"></a>
## For people unfamilar with Docker
Docker is not necessary to run Gamayun but it makes it much easier to do so. 
There are two tools that need to be installed to run examples from this repo with Docker:
 * ```docker```
 * ```docker-compose```

<a name="docker-low"></a>
### docker

The ```dockerfile``` in this repository looks roughly like this (note that there is also _arm64v8.dockerfile_ which looks much the same but has base image for arm64v8):
```dockerfile
# we are using already existing gamayun_py_utils image as base image (will be pulled from docker registry). 
# This image containes gamayun and utilities for reporting Gamayun job results from python scripts
FROM ibrko/gamayun_py_utils:0.2.0 

# copy everything from this repository to a /configuration folder in the docker container
COPY . /configuration

# set the env var so that Gamayun knows where to look for configuration
ENV GAMAYUN_CONF_ROOT /configuration
```

This dockerfile creates a image which will contain both Gamayun and configuration from this repo. When we start this image we get a container which is running Gamayun with this configuration. Note that no commands are needed to build this image as docker-compose takes care of that, as explained below.

<a name="docker-compose"></a>
### docker-compose

```docker-compose``` is a tool which allows easier composition of different containers. In our case, we have one container for Gamayun and one for MongoDB. These two containers need to communicate in order for Gamayun to store results to the database.

The ```docker-compose.yml``` that can be found in this repository does the following (note that there is also arm64v8.docker-compose.yml which is the same like this one except it builds image for arm64v8):
 * Defines a service (in docker-compose a synonym for a container) called ```mongodb-gamayun-sample``` which pulls official MongoDB image and runs it
   * The username and password of this database are set to _gamayun_ (change this if you are creating your configuration based on this repo)
   * We set the container to use a volume ```gamayun_db_sample``` and mount it to _/data/db_ directory (directory where MongoDB stores its data) in the container. Volumes are a way to connect filesystems on the host and in the container. At the bottom of the ```docker-compose.yml``` file is a section where we configure this volume and where we want it to map in the host filesystem. As path on host OS is something that is different for everyone that wants to run this sample, no path is configured in this sample configuration so Docker will select some path. For more information about how to set this path check [this SO question](https://stackoverflow.com/questions/36387032/how-to-set-a-path-on-host-for-a-named-volume-in-docker-compose-yml) and read Docker documentation 
   * We set the container to use network ```gamayun_sample_network``` which is configured at the bottom of the ```docker-compose.yml``` file. We don't expose this MongoDB container to outside world, only other containers connected to this network (our Gamayun container) is allowed to talk to it
 * Defines a service called ```gamayun``` which runs Gamayun application with our configuration. It doesn't pull the docker image from online repository, but rather builds it from the ```dockerfile``` in this repository (explained before).
   * This service (container) depends on ```mongodb-gamayun-sample``` service (container), so the database needs to run before the application
   * It mounts a volume for logs (so that logs are persisted to the host)
   * It is connected to ```gamayun_sample_network``` so it can't communicate to the outside world, but it can to other containers connected to this network (```mongodb-gamayun-sample```)
 * Configures network used for communication between containers and volumes

We can run all of this with ```docker-compose up``` in the root of this directory (note that this command might take a while the first time as it needs to build our docker image from ```dockerfile```). When everything is running, we can attach to of any of both containers with following commands:
 * ``` docker exec -it mongodb-gamayun-sample /bin/bash ```
   * if we want to connect to ```/bin/bash``` of the container that is running the database
 * ``` docker exec -it mongodb-gamayun-sample mongo -u <USERNAME> -p <PASSWORD> ```
   * if we want to connect directly to Mongo. Note that you need to set the username and password you set in the ```docker-compose.yml```. In this sample both are set to _gamayun_
 * ``` docker exec -it gamayun-sample /bin/bash ```
   * if we want to connect to ```/bin/bash``` of the container that is running the Gamayun application with provided configuration

<a name="python-scripts"></a>
# Python scripts
Python is used in this example, but any language/vm that has grpc support can be used instead (only the dockerfile needs to be modified to install apropriate packages). Protobuf files can be found in the [Gamayun main repo](https://github.com/ivan-brko/Gamayun).

However, for Python there is already Gamayun pip package that can be used for reporting job results or errors (repo can be found [here](https://github.com/ivan-brko/GamayunPyUtils)) which makes it easier to write scripts, so Python is the suggested way to write Gamayun jobs. This package is used in this sample configuration for result reports. 

<a name="sample-jobs"></a>
# Sample jobs
This configuration contains two sample jobs, one for scraping data from [r/programming](https://www.reddit.com/r/programming/) and other from [hackernews](https://news.ycombinator.com/).