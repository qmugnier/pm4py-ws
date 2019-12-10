A demo is publicly available at address (be careful!):
http://80.211.142.26/index.html
using the username 'admin01' and the password 'admin01'

HOW TO INSTALL FROM PIP:


pip install -U pm4pyws

Then, the script "main.py" could be launched with pre-defined log
In this case, the entire content of the "files" folder of this repository shall be there.


HOW TO BUILD ON SOURCES:


First of all install ANGULAR:

npm install -g @angular/cli
npm install -g @angular/material


PM4Py Web Services along with an Angular7(-8) web interface


To install the required NPM dependencies (also for building) enter the webapp/ folder and use the following command:

npm install


On Linux machines, also the following could be necessary:

sudo npm install --save-dev  --unsafe-perm node-sass


!!!!! Remember to change the IP address used by the web interface inside pm4py-service.service.ts !!!!!!



To compile the web interface, enter the webapp/ folder and use the following command
(it requires Node.JS 10, and Angular CLI):

ng build --prod



To run the web services and the web interface, use the command:

python main.py

And reach the URL http://localhost:5000/index.html
