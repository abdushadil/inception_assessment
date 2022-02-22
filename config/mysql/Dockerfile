# Container/Image name
FROM  mysql:5.6

# # Install apk
RUN apt-get update
RUN apt-get -y install vim tzdata python3-pip

# set timezone
ENV ENV="/root/.bashrc"
ENV USERNAME="inception"
ENV PASSWORD="inception"
ENV TZ=Africa/Khartoum

COPY ./config/mysql/add_user.sh /docker-entrypoint-initdb.d/add_user.sh

# Add alias
RUN echo 'alias ll="ls -al"' >> /root/.bashrc
RUN echo 'alias sql="mysql -u root -p"' >> /root/.bashrc
RUN echo 'alias python="python3"' >> /root/.bashrc
RUN echo 'alias pip="pip3"' >> /root/.bashrc
RUN echo 'alias add_user=". /docker-entrypoint-initdb.d/add_user.sh"' >> /root/.bashrc
