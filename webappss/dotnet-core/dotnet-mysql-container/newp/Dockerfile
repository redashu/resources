FROM mysql:5.7

ENV MYSQL_DATABASE=UserDB
ENV MYSQL_ROOT_PASSWORD=rootpassword

COPY abc.sql /docker-entrypoint-initdb.d/

# The official MySQL Docker image will automatically import .sql files from /docker-entrypoint-initdb.d/ on container startup

