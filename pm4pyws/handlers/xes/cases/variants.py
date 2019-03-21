from pm4py.statistics.traces.log import case_statistics


def get_statistics(log, parameters=None):
    """
    Gets the variants from the dataframe

    Parameters
    ------------
    log
        Log
    parameters
        Possible parameters of the algorithm

    Returns
    ------------
    variants
        Variants of the event log
    """
    if parameters is None:
        parameters = {}

    variants_statistics = case_statistics.get_variant_statistics(log, parameters=parameters)

    return variants_statistics
