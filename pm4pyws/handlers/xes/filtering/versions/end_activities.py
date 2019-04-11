from pm4py.algo.filtering.log.end_activities import end_activities_filter


def apply(log, filter, parameters=None):
    """
    Apply a filter to the current log (end activities filter)

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

    print("LOG END ACTIVITIES FILTER")

    return end_activities_filter.apply(log, filter[1], parameters=parameters)
