from pm4py.algo.filtering.log.timestamp import timestamp_filter
from datetime import datetime


def apply(log, filter, parameters=None):
    """
    Apply a timestamp filter to the log

    Parameters
    ------------
    log
        log where the filter should be applied
    filter
        Filter (two timestamps separated by @@@)
    parameters
        Parameters of the algorithm
    """
    if parameters is None:
        parameters = {}

    dt1 = str(datetime.utcfromtimestamp(int(filter[1].split("@@@")[0])))
    dt2 = str(datetime.utcfromtimestamp(int(filter[1].split("@@@")[1])))

    return timestamp_filter.filter_traces_intersecting(log, dt1, dt2, parameters=parameters)
