from pm4py.algo.discovery.dfg import factory as dfg_factory
from pm4py.visualization.dfg import factory as dfg_vis_factory
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.algo.filtering.log.auto_filter import auto_filter


def apply(log, parameters=None):
    """
    Gets the performance DFG

    Parameters
    ------------
    log
        Log
    parameters
        Parameters of the algorithm

    Returns
    ------------
    base64
        Base64 of an SVG representing the model
    model
        Text representation of the model
    format
        Format of the model
    """
    if parameters is None:
        parameters = {}

    filtered_log = auto_filter.apply_auto_filter(log, parameters=parameters)

    dfg = dfg_factory.apply(filtered_log, parameters=parameters)
    gviz = dfg_vis_factory.apply(dfg, log=log, variant="performance", parameters={"format": "svg"})

    return get_base64_from_gviz(gviz), None, ""
