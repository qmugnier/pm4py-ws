from pm4pyws.handlers.xes.filtering.versions import start_activities, end_activities, attributes_pos_trace, \
    attributes_neg_trace, attributes_pos_events, attributes_neg_events, variants


def apply(log, filter, parameters=None):
    """
    Apply a filter to the current log (factory method)

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

    if filter[0] == "start_activities":
        return start_activities.apply(log, filter, parameters=parameters)
    elif filter[0] == "end_activities":
        return end_activities.apply(log, filter, parameters=parameters)
    elif filter[0] == "attributes_pos_trace":
        return attributes_pos_trace.apply(log, filter, parameters=parameters)
    elif filter[0] == "attributes_neg_trace":
        return attributes_neg_trace.apply(log, filter, parameters=parameters)
    elif filter[0] == "attributes_pos_events":
        return attributes_pos_events.apply(log, filter, parameters=parameters)
    elif filter[0] == "attributes_neg_events":
        return attributes_neg_events.apply(log, filter, parameters=parameters)

    return log
