from flask import Flask, request, jsonify
from flask_cors import CORS

from pm4pyws.handlers.parquet.parquet import ParquetHandler

app = Flask(__name__, static_url_path='', static_folder='../webapp/dist/webapp')
app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file)
CORS(app)


class LogsHandlers:
    handlers = {}


@app.route("/getProcessSchema", methods=["GET"])
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


@app.route("/getCaseDurationGraph", methods=["GET"])
def get_case_duration():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    base64 = LogsHandlers.handlers[process].get_case_duration_svg()
    dictio = {"base64": base64.decode('utf-8')}
    ret = jsonify(dictio)
    return ret


@app.route("/getEventsPerTimeGraph", methods=["GET"])
def get_events_per_time():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    base64 = LogsHandlers.handlers[process].get_events_per_time_svg()
    dictio = {"base64": base64.decode('utf-8')}
    ret = jsonify(dictio)
    return ret


@app.route("/getSNA", methods=["GET"])
def get_sna():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    metric = request.args.get('metric', default='handover', type=str)
    threshold = request.args.get('threshold', default=0.0, type=float)

    print(request.args)

    sna = LogsHandlers.handlers[process].get_sna(variant=metric, parameters={"weight_threshold": threshold})
    return sna


@app.route("/getAllVariants", methods=["GET"])
def get_all_variants():
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    variants = LogsHandlers.handlers[process].get_variants()
    dictio = {"variants": variants}
    ret = jsonify(dictio)
    return ret


def load_log(log_name, file_path):
    if ".parque" in file_path:
        LogsHandlers.handlers[log_name] = ParquetHandler()
        LogsHandlers.handlers[log_name].build_from_path(file_path)
