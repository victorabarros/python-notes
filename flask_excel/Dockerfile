FROM python:3.7

COPY . /src
WORKDIR /src/app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
