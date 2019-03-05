from pm4pyws.handlers.parquet.process_schema.dfg_freq import get_vis as dfg_freq_vis

DFG_FREQ = "dfg_freq"

VERSIONS = {DFG_FREQ: dfg_freq_vis.apply}


def apply(dataframe, variant=DFG_FREQ, parameters=None):
    return VERSIONS[variant](dataframe, parameters=parameters)
