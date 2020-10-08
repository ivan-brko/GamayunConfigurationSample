FROM ibrko/gamayun_py_utils:0.2.0-arm64v8
COPY . /configuration
ENV GAMAYUN_CONF_ROOT /configuration