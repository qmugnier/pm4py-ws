from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.util import constants


def apply(dataframe, filter, parameters=None):
    """
    Apply a filter to the current log (attributes filter)

    Parameters
    ------------
    log
        Event log
    filter
        Filter to apply
    parameters
        Parameters of the algorithm

    Returns
    ------------
    log
        Event log
    """
    if parameters is None:
        parameters = {}

    parameters[constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY] = filter[1][0]
    parameters["positive"] = False

    return attributes_filter.apply(dataframe, filter[1][1], parameters=parameters)
