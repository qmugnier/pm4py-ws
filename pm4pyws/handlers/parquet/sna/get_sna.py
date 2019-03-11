from pm4py.algo.enhancement.sna import factory as sna_factory
from pm4py.visualization.common.utils import get_base64_from_file
from pm4py.visualization.sna import factory as sna_vis_factory


def apply(dataframe, variant="handover", parameters=None):
    """
    Gets the Social Network according to the specified metric and arc threshold

    Parameters
    -------------
    dataframe
        Dataframe
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

    metric = sna_factory.apply(dataframe, variant=variant, parameters=parameters)
    pyvis_repr = sna_vis_factory.apply(metric, variant="pyvis", parameters=parameters)

    return open(pyvis_repr).read()
