from pm4py.algo.filtering.log.variants import variants_filter


def apply(log, filter, parameters=None):
    """
    Apply a filter to the current log (variants filter)

    Parameters
    ------------
    log
        Log object
    filter
        Filter to apply
    parameters
        Parameters of the algorithm

    Returns
    ------------
    log
        Log object
    """
    if parameters is None:
        parameters = {}

    return variants_filter.apply(log, filter[1], parameters=parameters)
