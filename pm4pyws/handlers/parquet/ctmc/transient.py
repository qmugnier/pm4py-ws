from pm4py.objects.stochastic_petri import ctmc
from pm4py.visualization.transition_system import factory as ts_vis_factory
from pm4py.visualization.common.utils import get_base64_from_gviz


def apply(df, delay, parameters=None):
    """
    Perform CTMC simulation on a dataframe

    Parameters
    -------------
    df
        Dataframe
    delay
        Delay
    parameters
        Possible parameters of the algorithm

    Returns
    -------------
    graph
        Case duration graph
    """
    if parameters is None:
        parameters = {}

    tang_reach_graph, transient_analysis = ctmc.transient_analysis_from_dataframe(df, delay)
    viz = ts_vis_factory.apply(tang_reach_graph, parameters={"format": "svg",
                                                             "force_names": transient_analysis})

    return get_base64_from_gviz(viz)
