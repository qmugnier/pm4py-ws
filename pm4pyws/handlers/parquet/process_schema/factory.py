from pm4pyws.handlers.parquet.process_schema.dfg_freq import get_vis as dfg_freq_vis
from pm4pyws.handlers.parquet.process_schema.tree import get_vis as tree_vis
from pm4pyws.handlers.parquet.process_schema.petri_freq import get_vis as petri_freq_vis
from pm4pyws.handlers.parquet.process_schema.petri_perf import get_vis as petri_perf_vis

DFG_FREQ = "dfg_freq"
DFG_PERF = "dfg_perf"
TREE_FREQ = "tree_freq"
TREE_PERF = "tree_perf"
PETRI_FREQ = "petri_freq"
PETRI_PERF = "petri_perf"

VERSIONS = {DFG_FREQ: dfg_freq_vis.apply, DFG_PERF: dfg_freq_vis.apply, TREE_FREQ: tree_vis.apply,
            TREE_PERF: tree_vis.apply, PETRI_FREQ: petri_freq_vis.apply, PETRI_PERF: petri_perf_vis.apply}


def apply(dataframe, variant=DFG_FREQ, parameters=None):
    return VERSIONS[variant](dataframe, parameters=parameters)
