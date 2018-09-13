FROM debian:stretch-slim

RUN apt-get update                                                          \
 && apt-get install --yes --no-install-recommends                           \
        gnupg                                                               \
        wget                                                                \
                                                                            \
 && echo "deb http://yuma123.org/repos/apt/debian stretch main"             \
 >> /etc/apt/sources.list                                                   \
                                                                            \
 && wget -O - http://yuma123.org/repos/yuma123.gpg.key                      \
  | apt-key add                                                             \
                                                                            \
 && apt-get clean                                                           \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update                                                          \
 && apt-get install --yes --no-install-recommends                           \
        dos2unix                                                            \
        netconfd=2.11-0                                                     \
        openssh-server                                                      \
        openssl                                                             \
                                                                            \
 && apt-get clean                                                           \
 && rm -rf /var/lib/apt/lists/*

ADD netconf/netconfd-entrypoint.bash /

COPY YANG/als-popsicles-igloo.yang /usr/share/yuma/modules/

RUN dos2unix /netconfd-entrypoint.bash

ENV NETCONF_PORT=830                                                        \
                                                                            \
    NETCONF_USER=netconf                                                    \
    NETCONF_PASSWORD="netconf"                                              \
                                                                            \
    NETCONF_MODULES="als-popsicles-igloo"                           \
    NETCONF_STARTUP_CFG_FILE="startup-cfg.xml"                              \
                                                                            \
    NETCONF_LOG_LEVEL=info

EXPOSE 830

ENTRYPOINT [ "/bin/bash", "/netconfd-entrypoint.bash" ]
