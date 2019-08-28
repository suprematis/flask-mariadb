FROM python:3.7
RUN pip install flask && pip install PyMySQL 
WORKDIR /app
ADD ./app /app
CMD ["python", "./src/app.py"]
