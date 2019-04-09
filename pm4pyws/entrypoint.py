import sqlite3
import traceback
from threading import Semaphore

from flask import Flask, request, jsonify
from flask_cors import CORS

from pm4pyws.basic_user_management import BasicUserManagement
from pm4pyws.configuration import Configuration
from pm4pyws.handlers.parquet.parquet import ParquetHandler
from pm4pyws.handlers.xes.xes import XesHandler

um = BasicUserManagement()


class LogsHandlers:
    handlers = {}
    semaphore_matplot = Semaphore(1)


def check_session_validity(session_id):
    """
    Checks the validity of a session

    Parameters
    ------------
    session_id
        Session ID

    Returns
    ------------
    boolean
        Boolean value
    """
    if Configuration.enable_session:
        validity = um.check_session_validity(session_id)
        return True
    return True


def get_user_from_session(session_id):
    """
    Gets the user from the session

    Parameters
    ------------
    session_id
        Session ID

    Returns
    ------------
    user
        User ID
    """
    if Configuration.enable_session:
        user = um.get_user_from_session(session_id)
        return None
    return None


def check_is_admin(user):
    """
    Checks if the user is an administrator

    Parameters
    -------------
    user
        User

    Returns
    -------------
    boolean
        Boolean value
    """
    if Configuration.enable_session:
        return True
    return True


def check_user_log_visibility(user, process):
    """
    Checks if the user has visibility on the given process

    Parameters
    -------------
    user
        User
    process
        Process
    """
    if Configuration.enable_session:
        return True
    return True


def check_user_enabled_upload(user):
    """
    Checks if the user is enabled to upload a log

    Parameters
    ------------
    user
        User

    Returns
    ------------
    boolean
        Boolean value
    """
    if Configuration.enable_session:
        return True
    return True


def check_user_enabled_download(user, process):
    """
    Checks if the user is enabled to download a log

    Parameters
    ------------
    user
        User
    process
        Process

    Returns
    ------------
    boolean
        Boolean value
    """
    if Configuration.enable_session:
        return True
    return True


def load_log_static(log_name, file_path, parameters=None):
    """
    Loads an event log inside the known handlers

    Parameters
    ------------
    log_name
        Log name
    file_path
        Full path (in the services machine) to the log
    parameters
        Possible parameters
    """
    if log_name not in LogsHandlers.handlers:
        if file_path.endswith(".parquet"):
            LogsHandlers.handlers[log_name] = ParquetHandler()
            LogsHandlers.handlers[log_name].build_from_path(file_path, parameters=parameters)
        elif file_path.endswith(".csv"):
            LogsHandlers.handlers[log_name] = ParquetHandler()
            LogsHandlers.handlers[log_name].build_from_csv(file_path, parameters=parameters)
        elif file_path.endswith(".xes") or file_path.endswith(".xes.gz"):
            LogsHandlers.handlers[log_name] = XesHandler()
            LogsHandlers.handlers[log_name].build_from_path(file_path, parameters=parameters)


class PM4PyServices:
    app = Flask(__name__, static_url_path='', static_folder='../webapp/dist/webapp')
    app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static',
                     view_func=app.send_static_file)
    CORS(app)

    def load_log(self, log_name, file_path, parameters=None):
        """
        Loads an event log inside the known handlers

        Parameters
        ------------
        log_name
            Log name
        file_path
            Full path (in the services machine) to the log
        parameters
            Possible parameters
        """
        load_log_static(log_name, file_path, parameters=parameters)

    def serve(self, host="0.0.0.0", port="5000", threaded=True):
        self.app.run(host=host, port=port, threaded=threaded)


@PM4PyServices.app.route("/getProcessSchema", methods=["GET"])
def get_process_schema():
    """
    Gets the process schema in the wanted format

    Returns
    ------------
    dictio
        JSONified dictionary that contains in the 'base64' entry the SVG representation
        of the process schema. Moreover, 'model' contains the process model (if the output is meaningful)
        and 'format' contains the format
    :return:
    """
    dictio = {}
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            # reads the decoration
            decoration = request.args.get('decoration', default='freq', type=str)
            # reads the typeOfModel
            type_of_model = request.args.get('typeOfModel', default='dfg', type=str)
            # reads the simplicity
            simplicity = request.args.get('simplicity', default=0.6, type=float)
            variant = type_of_model + "_" + decoration
            parameters = {"decreasingFactor": simplicity}
            base64, model, format, this_handler = LogsHandlers.handlers[process].get_schema(variant=variant,
                                                                                            parameters=parameters)
            if model is not None:
                model = model.decode('utf-8')
            dictio = {"base64": base64.decode('utf-8'), "model": model, "format": format, "handler": this_handler}
    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/getCaseDurationGraph", methods=["GET"])
def get_case_duration():
    """
    Gets the Case Duration graph

    Returns
    ------------
    dictio
        JSONified dictionary that contains in the 'base64' entry the SVG representation
        of the case duration graph
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}
    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            LogsHandlers.semaphore_matplot.acquire()
            try:
                base64 = LogsHandlers.handlers[process].get_case_duration_svg()
                dictio = {"base64": base64.decode('utf-8')}
            except:
                traceback.print_exc()
                dictio = {"base64": ""}
            LogsHandlers.semaphore_matplot.release()

    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/getEventsPerTimeGraph", methods=["GET"])
def get_events_per_time():
    """
    Gets the Event per Time graph

    Returns
    -------------
    dictio
        JSONified dictionary that contains in the 'base64' entry the SVG representation
        of the events per time graph
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            LogsHandlers.semaphore_matplot.acquire()
            try:
                base64 = LogsHandlers.handlers[process].get_events_per_time_svg()
                dictio = {"base64": base64.decode('utf-8')}
            except:
                traceback.print_exc()
                dictio = {"base64": ""}
            LogsHandlers.semaphore_matplot.release()

    ret = jsonify(dictio)

    return ret


@PM4PyServices.app.route("/getSNA", methods=["GET"])
def get_sna():
    """
    Gets the Social Network (Pyvis) representation of the event log

    Returns
    -----------
    html
        HTML page containing the SNA representation
    """
    try:
        # reads the session
        session = request.args.get('session', type=str)
        # reads the requested process name
        process = request.args.get('process', default='receipt', type=str)
        sna = ""

        if check_session_validity(session):
            user = get_user_from_session(session)
            if check_user_log_visibility(user, process):
                metric = request.args.get('metric', default='handover', type=str)
                threshold = request.args.get('threshold', default=0.0, type=float)
                sna = LogsHandlers.handlers[process].get_sna(variant=metric, parameters={"weight_threshold": threshold})
    except:
        traceback.print_exc()
        sna = ""

    return sna


@PM4PyServices.app.route("/getAllVariants", methods=["GET"])
def get_all_variants():
    """
    Gets all the variants from the event log

    Returns
    ------------
    dictio
        JSONified dictionary that contains in the 'variants' entry the list of variants
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            variants = LogsHandlers.handlers[process].get_variant_statistics()
            dictio = {"variants": variants}

    ret = jsonify(dictio)

    return ret


@PM4PyServices.app.route("/getAllCases", methods=["GET"])
def get_all_cases():
    """
    Gets all the cases from the event log

    Returns
    ------------
    dictio
        JSONified dictionary that contains in the 'cases' entry the list of cases
    """
    # reads the session
    session = request.args.get('session', type=str)
    process = request.args.get('process', default='receipt', type=str)
    variant = request.args.get('variant', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            parameters = {}
            if variant is not None:
                parameters["variant"] = variant
            cases_list = LogsHandlers.handlers[process].get_case_statistics(parameters=parameters)
            dictio = {"cases": cases_list}
    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/getEvents", methods=["GET"])
def get_events():
    """
    Gets the events from a Case ID

    Returns
    -------------
    dictio
        JSONified dictionary that contains in the 'events' entry the list of events
    """
    # reads the session
    session = request.args.get('session', type=str)
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            caseid = request.args.get('caseid', type=str)
            events = LogsHandlers.handlers[process].get_events(caseid)
            i = 0
            while i < len(events):
                keys = list(events[i].keys())
                for key in keys:
                    if str(events[i][key]).lower() == "nan" or str(events[i][key]).lower() == "nat":
                        del events[i][key]
                i = i + 1
            dictio = {"events": events}
    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/loadLogFromPath", methods=["POST"])
def load_log_from_path():
    """
    Service that loads a log from a path
    """
    if Configuration.enable_load_local_path:
        try:
            # reads the session
            session = request.args.get('session', type=str)

            if check_session_validity(session):
                user = get_user_from_session(session)

                # reads the log_name entry from the request JSON
                log_name = request.json["log_name"]
                # reads the log_path entry from the request JSON
                log_path = request.json["log_path"]
                parameters = request.json["parameters"] if "parameters" in request.json else None
                print("log_name = ", log_name, "log_path = ", log_path)
                load_log_static(log_name, log_path, parameters=parameters)
                return "OK"
        except:
            traceback.print_exc()
            return "FAIL"
    return "FAIL"


@PM4PyServices.app.route("/getLogsList", methods=["GET"])
def get_logs_list():
    """
    Gets the list of logs loaded into the system

    Returns
    -----------
    dictio
        JSONified dictionary that contains in the 'logs' entry the list of events logs
    """
    # reads the session
    session = request.args.get('session', type=str)
    return jsonify({"logs": list(LogsHandlers.handlers.keys())})


@PM4PyServices.app.route("/transientAnalysis", methods=["GET"])
def do_transient_analysis():
    """
    Perform transient analysis on the log

    Returns
    ------------
    dictio
        JSONified dictionary that contains in the 'base64' entry the SVG representation
        of the events per time graph
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            delay = request.args.get('delay', default=86400, type=float)

            base64 = LogsHandlers.handlers[process].get_transient(delay)
            dictio = {"base64": base64.decode('utf-8')}

    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/getLogSummary", methods=["GET"])
def get_log_summary():
    """
    Gets a summary of the log

    Returns
    ------------
    log_summary
        Log summary
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            this_variants_number = LogsHandlers.handlers[process].variants_number
            this_cases_number = LogsHandlers.handlers[process].cases_number
            this_events_number = LogsHandlers.handlers[process].events_number

            ancestor_variants_number = LogsHandlers.handlers[process].first_ancestor.variants_number
            ancestor_cases_number = LogsHandlers.handlers[process].first_ancestor.cases_number
            ancestor_events_number = LogsHandlers.handlers[process].first_ancestor.events_number

            dictio = {"this_variants_number": this_variants_number, "this_cases_number": this_cases_number,
                      "this_events_number": this_events_number, "ancestor_variants_number": ancestor_variants_number,
                      "ancestor_cases_number": ancestor_cases_number, "ancestor_events_number": ancestor_events_number}

    ret = jsonify(dictio)
    return ret


@PM4PyServices.app.route("/downloadXesLog", methods=["GET"])
def download_xes_log():
    """
    Download the XES log

    Returns
    ------------
    xes_log
        XES log
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    if Configuration.enable_download:
        if check_session_validity(session):
            user = get_user_from_session(session)
            if check_user_log_visibility(user, process):
                if check_user_enabled_download(user, process):
                    content = LogsHandlers.handlers[process].download_xes_log()
                    return jsonify({"content": content.decode('utf-8')})
        return jsonify({"content": ""})


@PM4PyServices.app.route("/downloadCsvLog", methods=["GET"])
def download_csv_log():
    """
    Download the CSV log

    Returns
    ------------
    csv_log
        CSV log
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)
    if Configuration.enable_download:
        if check_session_validity(session):
            user = get_user_from_session(session)
            if check_user_log_visibility(user, process):
                if check_user_enabled_download(user, process):
                    content = LogsHandlers.handlers[process].download_csv_log()
                    return jsonify({"content": content})
    return jsonify({"content": ""})


@PM4PyServices.app.route("/getAlignmentsVisualizations", methods=["POST"])
def get_alignments():
    """
    Get alignments visualizations

    Returns
    -------------
    dictio
        Dictionary containing the Petri net and the table
    """
    # reads the session
    session = request.args.get('session', type=str)
    # reads the requested process name
    process = request.args.get('process', default='receipt', type=str)

    dictio = {}

    if check_session_validity(session):
        user = get_user_from_session(session)
        if check_user_log_visibility(user, process):
            petri_string = request.json["model"]
            svg_on_petri, svg_table = LogsHandlers.handlers[process].get_alignments(petri_string, parameters={})
            dictio = {"petri": svg_on_petri.decode('utf-8'), "table": svg_table.decode('utf-8')}

    ret = jsonify(dictio)

    return ret
