FROM python:3.8.8

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

ENTRYPOINT ["python"]

CMD ["flask_app.py"]


