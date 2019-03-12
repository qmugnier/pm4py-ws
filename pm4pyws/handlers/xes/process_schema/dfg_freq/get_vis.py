from pm4py.algo.discovery.dfg import factory as dfg_factory
from pm4py.visualization.dfg import factory as dfg_vis_factory
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.algo.filtering.log.auto_filter import auto_filter
from pm4py.algo.filtering.log.attributes import attributes_filter

from pm4pyws.util import constants

def apply(log, parameters=None):
    """
    Gets the frequency DFG

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

    log = attributes_filter.filter_log_on_max_no_activities(log, max_no_activities=constants.MAX_NO_ACTIVITIES,
                                                            parameters=parameters)
    filtered_log = auto_filter.apply_auto_filter(log, parameters=parameters)

    dfg = dfg_factory.apply(filtered_log, parameters=parameters)
    gviz = dfg_vis_factory.apply(dfg, log=log, variant="frequency", parameters={"format": "svg"})

    return get_base64_from_gviz(gviz), None, ""
