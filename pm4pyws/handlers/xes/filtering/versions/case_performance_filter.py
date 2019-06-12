from pm4py.algo.filtering.log.cases import case_filter
from pm4py.util import constants as pm4_constants
from pm4py.objects.log.util import xes


def apply(log, filter, parameters=None):
    """
    Applies a filter on case performance

    Parameters
    --------------
    log
        Log
    filter
        Filter (two performance bounds separated by @@@)
    parameters
        Parameters of the algorithm

    Returns
    ---------------
    filtered_log
        Filtered log
    """
    if parameters is None:
        parameters = {}

    min_case_performance = float(filter[1].split("@@@")[0])
    max_case_performance = float(filter[1].split("@@@")[1])

    return case_filter.filter_on_case_performance(log, min_case_performance, max_case_performance,
                                                  parameters=parameters)
