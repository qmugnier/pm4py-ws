from pm4py.algo.enhancement.sna import factory as sna_factory
from pm4py.visualization.sna import factory as sna_vis_factory


def apply(log, variant="handover", parameters=None):
    """
    Gets the Social Network according to the specified metric and arc threshold

    Parameters
    -------------
    log
        Log
    variant
        Variant of the algorithm to use
    parameters
        Possible parameters of the algorithm (arc threshold)

    Returns
    -------------
    sna
        Social Network representation
    """
    if parameters is None:
        parameters = {}

    parameters["metric_normalization"] = True

    metric = sna_factory.apply(log, variant=variant, parameters=parameters)
    pyvis_repr = sna_vis_factory.apply(metric, variant="pyvis", parameters=parameters)

    return open(pyvis_repr).read()
