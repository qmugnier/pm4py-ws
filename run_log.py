import os
import webbrowser
from sys import argv

import requests

from pm4pyws.entrypoint import PM4PyServices

# local host of the current machine
THIS_HOST = "127.0.0.1"
# web pages location
WEB_PAGES = "http://www.alessandroberti.it/webapp"
# host that shall be listening (0.0.0.0 means accepting connections from everything)
LISTENING_HOST = "0.0.0.0"
# listen to this port
LISTENING_PORT = 5000

if __name__ == "__main__":
    log_path = argv[1]
    log_name = os.path.basename(os.path.normpath(log_path)).split(".")[0]

    try:
        # try to see if the service is alive, in that case just try to add the 'receipt'
        # process to the list
        r = requests.post("http://" + THIS_HOST + ":" + str(LISTENING_PORT) + "/loadLogFromPath",
                          json={"log_name": log_name,
                                "log_path": log_path})
        print("service listening, told to load the log, response: " + str(r.text))
        webbrowser.open(WEB_PAGES + "/index.html")
    except:
        # otherwise, the service is not listening and it needs to be boot up
        print("service not listening, booting it up")
        import pm4py
        print("version of PM4Py: ",pm4py.__version__)
        S = PM4PyServices()
        # loads the process into the services
        S.load_log(log_name, log_path)
        # offers the service to the outside
        webbrowser.open(WEB_PAGES + "/index.html")
        S.serve(host=LISTENING_HOST, port=LISTENING_PORT)
