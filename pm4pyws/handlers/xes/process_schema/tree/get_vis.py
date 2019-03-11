from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.visualization.process_tree import factory as pt_vis_factory


def apply(log, parameters=None):
    """
    Gets the process tree using Inductive Miner Directly-Follows

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
    tree = inductive_miner.apply_tree(log, parameters=parameters)
    gviz = pt_vis_factory.apply(tree, parameters={"format": "svg"})
    return get_base64_from_gviz(gviz), None, ""

