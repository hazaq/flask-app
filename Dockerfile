FROM ubuntu:latest
MAINTAINER none
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
