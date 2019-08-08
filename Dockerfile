FROM tiangolo/uwsgi-nginx-flask

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install nano vim git python3-pydot python-pydot python-pydot-ng graphviz python3-tk zip unzip

RUN pip install --no-cache-dir -U pm4py pm4pycvxopt Flask flask-cors requests python-keycloak pyinstaller PyQT5 setuptools pm4pybpmn
COPY . /app
#RUN cd /app/webapp2 && git checkout master && git pull
#RUN mkdir -p /app/webapp2
#RUN rm -rRf /app/webapp2
#RUN git clone https://github.com/pm-tk/source.git
#RUN mv /source /app/webapp2
#RUN cd /app/webapp2 && npm install && npm install --save-dev --unsafe-perm node-sass && npm install -g @angular/cli & npm install -g @angular/material
#RUN cd /app/webapp2 && ng build --prod

#RUN cd /app/webapp2 && wget http://www.alessandroberti.it/dist.tar && tar xvf dist.tar

RUN cd /app && python setup.py install
