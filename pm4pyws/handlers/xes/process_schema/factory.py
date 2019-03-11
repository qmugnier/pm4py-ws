DFG_FREQ = "dfg_freq"
DFG_PERF = "dfg_perf"
TREE_FREQ = "tree_freq"
TREE_PERF = "tree_perf"
INDUCTIVE_FREQ = "inductive_freq"
INDUCTIVE_PERF = "inductive_perf"
ALPHA_FREQ = "alpha_freq"
ALPHA_PERF = "alpha_perf"

VERSIONS = {}


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
