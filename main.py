from pm4pyws.entrypoint import PM4PyServices
import requests


THIS_HOST = "127.0.0.1"
LISTENING_HOST = "0.0.0.0"
LISTENING_PORT = 5000

if __name__ == "__main__":
    try:
        r = requests.post("http://" + THIS_HOST + ":" + str(LISTENING_PORT) + "/loadLogFromPath", json={"log_name": "receipt",
                                                                                                   "log_path": "receipt.parquet"})
        print("service listening, told to load the log, response: "+str(r.text))
    except:
        print("service not listening, booting it up")
        S = PM4PyServices()
        S.load_log("receipt", "receipt.parquet")
        S.serve(host=LISTENING_HOST, port=LISTENING_PORT)