FROM ubuntu
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python python-pip supervisor uwsgi libffi-dev
EXPOSE 5000
ADD . /opt/apps/carrier_test
RUN pip install -r /opt/apps/carrier_test/requirements.txt
RUN chown -R www-data:www-data /opt/apps/carrier_test
CMD ["/bin/sh", "-e", "/opt/apps/carrier_test/run"]