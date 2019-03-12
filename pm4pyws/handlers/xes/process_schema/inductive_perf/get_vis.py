from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.objects.petri.exporter.pnml import export_petri_as_string
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.visualization.petrinet import factory as pn_vis_factory
from pm4py.algo.filtering.log.auto_filter import auto_filter


def apply(log, parameters=None):
    """
    Gets the Petri net through Inductive Miner, decorated by performance metric

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

    net, im, fm = inductive_miner.apply(filtered_log, parameters=parameters)
    gviz = pn_vis_factory.apply(net, im, fm, log=log, variant="performance", parameters={"format": "svg"})

    svg = get_base64_from_gviz(gviz)

    return svg, export_petri_as_string(net, im, fm), ".pnml"
