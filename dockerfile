FROM ibrko/gamayun_py_utils:0.2.0
COPY . /configuration
ENV GAMAYUN_CONF_ROOT /configuration