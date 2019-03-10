from pm4pyws.handlers.parquet.process_schema.dfg_freq import get_vis as dfg_freq_vis
from pm4pyws.handlers.parquet.process_schema.dfg_perf import get_vis as dfg_perf_vis
from pm4pyws.handlers.parquet.process_schema.tree import get_vis as tree_vis
from pm4pyws.handlers.parquet.process_schema.inductive_freq import get_vis as petri_freq_vis
from pm4pyws.handlers.parquet.process_schema.inductive_perf import get_vis as petri_perf_vis

DFG_FREQ = "dfg_freq"
DFG_PERF = "dfg_perf"
TREE_FREQ = "tree_freq"
TREE_PERF = "tree_perf"
INDUCTIVE_FREQ = "inductive_freq"
INDUCTIVE_PERF = "inductive_perf"

VERSIONS = {DFG_FREQ: dfg_freq_vis.apply, DFG_PERF: dfg_perf_vis.apply, TREE_FREQ: tree_vis.apply,
            TREE_PERF: tree_vis.apply, INDUCTIVE_FREQ: petri_freq_vis.apply, INDUCTIVE_PERF: petri_perf_vis.apply}


def apply(dataframe, variant=DFG_FREQ, parameters=None):
    return VERSIONS[variant](dataframe, parameters=parameters)
