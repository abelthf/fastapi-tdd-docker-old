# pull official base image
FROM postgres:14.3-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

