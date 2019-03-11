from pm4py.statistics.traces.log import case_statistics
from pm4py.visualization.common.utils import get_base64_from_file
from pm4py.visualization.graphs import factory as graphs_factory


def get_case_duration_svg(log, parameters=None):
    """
    Gets the SVG of the case duration graph

    Parameters
    -------------
    log
        Log
    parameters
        Possible parameters of the algorithm

    Returns
    -------------
    graph
        Case duration graph
    """
    if parameters is None:
        parameters = {}

    x, y = case_statistics.get_kde_caseduration(log, parameters)
    gviz = graphs_factory.apply_plot(x, y, variant="cases", parameters={"format": "svg"})

    return get_base64_from_file(gviz)
