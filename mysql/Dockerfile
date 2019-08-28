FROM mysql:5.7.27
COPY ./docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
COPY ./custom /etc/mysql/conf.d/
#RUN []
#CMD ["mysql", "-uroot","-e", "CREATE DATABASE flasktest; GRANT ALL ON flasktest.* TO flaskuser@localhost IDENTIFIED BY 'flask123'; FLUSH PRIVILEGES;"]
#CMD ["sleep", "30", "mysql", "-uroot", "-e", "CREATE DATABASE flasktest; GRANT ALL ON flasktest.* TO flaskuser@localhost IDENTIFIED BY 'flask123'; FLUSH PRIVILEGES;" ]
#CMD sleep 30
