from pm4pyws.handlers.xes.process_schema.alpha_freq import get_vis as alpha_freq_vis
from pm4pyws.handlers.xes.process_schema.alpha_performance import get_vis as alpha_perf_vis
from pm4pyws.handlers.xes.process_schema.dfg_freq import get_vis as dfg_freq_vis
from pm4pyws.handlers.xes.process_schema.dfg_perf import get_vis as dfg_perf_vis
from pm4pyws.handlers.xes.process_schema.inductive_freq import get_vis as inductive_freq_vis
from pm4pyws.handlers.xes.process_schema.inductive_perf import get_vis as inductive_perf_vis
from pm4pyws.handlers.xes.process_schema.tree import get_vis as tree_vis

DFG_FREQ = "dfg_freq"
DFG_PERF = "dfg_perf"
TREE_FREQ = "tree_freq"
TREE_PERF = "tree_perf"
INDUCTIVE_FREQ = "inductive_freq"
INDUCTIVE_PERF = "inductive_perf"
ALPHA_FREQ = "alpha_freq"
ALPHA_PERF = "alpha_perf"

VERSIONS = {DFG_FREQ: dfg_freq_vis.apply, DFG_PERF: dfg_perf_vis.apply, TREE_FREQ: tree_vis.apply,
            TREE_PERF: tree_vis.apply, INDUCTIVE_FREQ: inductive_freq_vis.apply,
            INDUCTIVE_PERF: inductive_perf_vis.apply, ALPHA_FREQ: alpha_freq_vis.apply,
            ALPHA_PERF: alpha_perf_vis.apply}


def apply(log, variant=DFG_FREQ, parameters=None):
    """
    Factory method to get a (decorated) process schema

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
    return VERSIONS[variant](log, parameters=parameters)
