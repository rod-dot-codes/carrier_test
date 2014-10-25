FROM debian:wheezy
RUN apt-get update
RUN apt-get install -y python python-pip supervisor uwsgi libffi-dev python-dev
EXPOSE 5000
ADD . /opt/apps/carrier_test
ADD supervisor.conf /opt/supervisor.conf
ADD run.sh /usr/local/bin/run

RUN pip install -r /opt/apps/carrier_test/requirements.txt
RUN chown -R www-data:www-data /opt/apps/carrier_test
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]