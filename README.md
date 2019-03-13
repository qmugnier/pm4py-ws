HOW TO INSTALL THE BINARY DISTRIBUTION:

pip install -U Flask flask-cors pm4py
pip install -U pm4pyws

At this point, you could use the script "main.py" as reference to start the service with some logs preloaded,
or to enable double-click-opening .xes and/or .parquet in Windows,
put both the "run_log.py" and "run_log.bat" (changing the paths to python in an opportune way)
in C: and associate to .xes and/or .parquet the run_log.bat opener.


HOW TO BUILD ON SOURCES:


First of all install ANGULAR:

npm install -g @angular/cli


PM4Py Web Services along with an Angular7 web interface

A (almost) last build could be found on http://194.32.77.109:5000/index.html


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