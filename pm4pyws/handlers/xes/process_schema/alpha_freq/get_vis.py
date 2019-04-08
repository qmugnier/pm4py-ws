from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.algo.filtering.log.auto_filter import auto_filter
from pm4py.objects.petri.exporter.pnml import export_petri_as_string
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.visualization.petrinet import factory as pn_vis_factory

from pm4pyws.util import constants


def apply(log, parameters=None):
    """
    Gets the Petri net through Alpha Miner, decorated by frequency metric

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

    net, im, fm = alpha_miner.apply(filtered_log, parameters=parameters)
    parameters["format"] = "svg"
    gviz = pn_vis_factory.apply(net, im, fm, log=log, variant="frequency", parameters=parameters)

    svg = get_base64_from_gviz(gviz)

    return svg, export_petri_as_string(net, im, fm), ".pnml", "xes"
