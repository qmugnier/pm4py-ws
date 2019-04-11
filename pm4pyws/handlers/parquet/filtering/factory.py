from pm4pyws.handlers.parquet.filtering.versions import start_activities, end_activities


def apply(dataframe, filter, parameters=None):
    """
    Apply a filter to the current log (factory method)

    Parameters
    ------------
    dataframe
        Pandas dataframe
    filter
        Filter to apply
    parameters
        Parameters of the algorithm

    Returns
    ------------
    dataframe
        Pandas dataframe
    """
    if parameters is None:
        parameters = {}

    if filter[0] == "start_activities":
        return start_activities.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "end_activities":
        return end_activities.apply(dataframe, filter, parameters=parameters)

    return dataframe
