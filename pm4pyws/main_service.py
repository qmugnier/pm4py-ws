from flask import Flask, request
from flask_cors import CORS

from pm4pyws.handlers.parquet.parquet import ParquetHandler

app = Flask(__name__)
CORS(app)


class LogsHandlers:
    handlers = {}


@app.route("/getProcessSchema", methods=["GET"])
def get_process_schema():
    # reads the requested process name
    process = request.args.get('process', default='roadtraffic', type=str)
    # reads the variant
    variant = request.args.get('variant', default='dfg_freq', type=str)

    return LogsHandlers.handlers[process].get_schema(variant=variant)


def load_log(log_name, file_path):
    if ".parque" in file_path:
        LogsHandlers.handlers[log_name] = ParquetHandler(file_path)
