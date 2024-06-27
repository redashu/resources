FROM mysql:5.7

ENV MYSQL_DATABASE=UserDB
ENV MYSQL_ROOT_PASSWORD=Redhat@123

COPY abc.sql /docker-entrypoint-initdb.d/