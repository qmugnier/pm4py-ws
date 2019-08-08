FROM tiangolo/uwsgi-nginx-flask

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install nano vim git python3-pydot python-pydot python-pydot-ng graphviz python3-tk zip unzip curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install nodejs

RUN pip install --no-cache-dir -U pm4py pm4pycvxopt Flask flask-cors requests python-keycloak pyinstaller PyQT5 setuptools pm4pybpmn
COPY . /app
RUN mkdir -p /app/webapp2
RUN rm -rRf /app/webapp2
RUN cd / && git clone https://github.com/pm-tk/source.git
RUN ls -l /
RUN cd / && mv /source /app/webapp2
RUN cd /app/webapp2 && npm install && npm install --save-dev --unsafe-perm node-sass && npm install -g @angular/core @angular/cli @angular/material
RUN cd /app/webapp2 && ng build --prod

#RUN cd /app/webapp2 && wget http://www.alessandroberti.it/dist.tar && tar xvf dist.tar

RUN cd /app && python setup.py install
