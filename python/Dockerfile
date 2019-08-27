FROM python:3.7
WORKDIR /app
COPY ./app /app
RUN pip install flask && pip install mysqlclient
CMD ["/bin/bash", "-c", "sleep 10"]
CMD ["python", "./src/app.py"]
