# Sample configuration for Gamayun
This repo contains a minimal sample configuration for Gamayun Data collector, which can be used as a base for creation of new configuration.
<br>
Gamayun main repo: https://github.com/ivan-brko/Gamayun

# Docker
While Gamayun can be run locally, it is easiest to run it with Docker and this repository contains all the needed docker files.

Gamayun docker image is used as a base for an image which contains this configuration and docker-compose is setup to run Gamayun (with this configuration) and MongoDB and to connect them. 

To run all of this, position your terminal in the root of this directory and run:
```docker
docker-compose -f docker-compose.yml up
```
If any other packages are missing (like maybe python packages for web-scrapping 🙂) just add a line that installs that package for Alpine (or maybe for pip) in the dockerfile.

# Python script
Python is used in this example, but anything that has grpc support can be used instead (only the dockerfile needs to be modified to install apropriate packages). Protobuf files can be found in the Gamayun repo.

At the moment _GamayunResult_pb2.py_ and _GamayunResult_pb2_grpc.py_ files neeed to be copied by hand for each script but later on these will be added as packages to Python and installed in the image.
