from flask import Flask, request, jsonify
from flask_cors import CORS

from pm4pyws.handlers.parquet.parquet import ParquetHandler
from threading import Semaphore

class LogsHandlers:
    handlers = {}
    semaphore_matplot = Semaphore(1)


def load_log_static(log_name, file_path, parameters=None):
    if log_name not in LogsHandlers.handlers:
        if file_path.endswith(".parquet"):
            LogsHandlers.handlers[log_name] = ParquetHandler()
            LogsHandlers.handlers[log_name].build_from_path(file_path, parameters=parameters)
        elif file_path.endswith(".csv"):
            LogsHandlers.handlers[log_name] = ParquetHandler()
            LogsHandlers.handlers[log_name].build_from_csv(file_path, parameters=parameters)


class PM4PyServices:
    app = Flask(__name__, static_url_path='', static_folder='../webapp/dist/webapp')
    app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static',
                     view_func=app.send_static_file)
    CORS(app)

    def load_log(self, log_name, file_path, parameters=None):
        load_log_static(log_name, file_path, parameters=parameters)

    def serve(self, host="0.0.0.0", port="5000", threaded=True):
        self.app.run(host=host, port=port, threaded=threaded)


@PM4PyServices.app.route("/getProcessSchema", methods=["GET"])
def get_process_schema():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    # reads the decoration
    decoration = request.args.get('decoration', default='freq', type=str)
    # reads the typeOfModel
    type_of_model = request.args.get('typeOfModel', default='dfg', type=str)
    # reads the simplicity
    simplicity = request.args.get('simplicity', default=0.6, type=float)
    print(request.args)
    variant = type_of_model + "_" + decoration
    parameters = {"decreasingFactor": simplicity}
    base64 = LogsHandlers.handlers[process].get_schema(variant=variant, parameters=parameters)
    dictio = {"base64": base64.decode('utf-8')}
    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/getCaseDurationGraph", methods=["GET"])
def get_case_duration():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    LogsHandlers.semaphore_matplot.acquire()
    try:
        base64 = LogsHandlers.handlers[process].get_case_duration_svg()
        dictio = {"base64": base64.decode('utf-8')}
    except:
        dictio = {"base64": ""}
    LogsHandlers.semaphore_matplot.release()

    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/getEventsPerTimeGraph", methods=["GET"])
def get_events_per_time():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    LogsHandlers.semaphore_matplot.acquire()
    try:
        base64 = LogsHandlers.handlers[process].get_events_per_time_svg()
        dictio = {"base64": base64.decode('utf-8')}
    except:
        dictio = {"base64": ""}
    LogsHandlers.semaphore_matplot.release()

    ret = jsonify(dictio)

    return ret


@PM4PyServices.app.route("/getSNA", methods=["GET"])
def get_sna():
    try:
        # reads the requested process name
        process = request.args.get('process', default='receipt', type=str)
        metric = request.args.get('metric', default='handover', type=str)
        threshold = request.args.get('threshold', default=0.0, type=float)

        print(request.args)

        sna = LogsHandlers.handlers[process].get_sna(variant=metric, parameters={"weight_threshold": threshold})
    except:
        sna = ""

    return sna


@PM4PyServices.app.route("/getAllVariants", methods=["GET"])
def get_all_variants():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    variants = LogsHandlers.handlers[process].get_variants()
    dictio = {"variants": variants}
    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/loadLogFromPath", methods=["POST"])
def load_log_from_path():
    try:
        log_name = request.json["log_name"]
        log_path = request.json["log_path"]
        print("log_name = ", log_name, "log_path = ", log_path)
        load_log_static(log_name, log_path)
    except:
        return "FAIL"
    return "OK"


@PM4PyServices.app.route("/getLogsList", methods=["GET"])
def get_logs_list():
    return jsonify({"logs": list(LogsHandlers.handlers.keys())})