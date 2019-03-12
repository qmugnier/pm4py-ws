from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.objects.petri.exporter.pnml import export_petri_as_string
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.visualization.petrinet import factory as pn_vis_factory


def apply(log, parameters=None):
    if parameters is None:
        parameters = {}

    net, im, fm = inductive_miner.apply(log, parameters=parameters)
    gviz = pn_vis_factory.apply(net, im, fm, log=log, variant="performance", parameters={"format": "svg"})

    svg = get_base64_from_gviz(gviz)

    return svg, export_petri_as_string(net, im, fm), ".pnml"
