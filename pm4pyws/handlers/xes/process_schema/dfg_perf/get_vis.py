from pm4py.algo.discovery.dfg import factory as dfg_factory
from pm4py.visualization.dfg import factory as dfg_vis_factory
from pm4py.visualization.common.utils import get_base64_from_gviz


def apply(log, parameters=None):
    if parameters is None:
        parameters = {}
    dfg = dfg_factory.apply(log, parameters=parameters)
    gviz = dfg_vis_factory.apply(dfg, log=log, variant="performance", parameters={"format": "svg"})

    return get_base64_from_gviz(gviz), None, ""
