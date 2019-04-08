from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.algo.filtering.log.auto_filter import auto_filter
from pm4py.objects.heuristics_net.net import HeuristicsNet
from pm4py.visualization.common.utils import get_base64_from_file
from pm4py.visualization.heuristics_net import factory as heu_vis_factory
from pm4py.algo.discovery.dfg import factory as dfg_factory

from pm4pyws.util import constants


def apply(log, parameters=None):
    """
    Gets the performance HNet

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

    dfg_freq = dfg_factory.apply(filtered_log, parameters=parameters)
    dfg_perf = dfg_factory.apply(filtered_log, variant="performance", parameters=parameters)

    heu_net = HeuristicsNet(dfg_freq, performance_dfg=dfg_perf)

    heu_net.calculate()

    vis = heu_vis_factory.apply(heu_net, parameters={"format": "svg"})

    return get_base64_from_file(vis.name), None, "", "xes"
