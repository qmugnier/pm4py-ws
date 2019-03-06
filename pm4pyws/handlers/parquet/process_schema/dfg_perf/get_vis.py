from pm4py.algo.discovery.dfg.adapters.pandas import df_statistics
from pm4py.visualization.dfg import factory as dfg_vis_factory
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.algo.filtering.pandas.attributes import attributes_filter
from pm4py.objects.log.util import xes
from pm4py.algo.filtering.pandas.auto_filter import auto_filter


def apply(dataframe, parameters=None):
    if parameters is None:
        parameters = {}
    dataframe = auto_filter.apply_auto_filter(dataframe, parameters=parameters)
    dfg = df_statistics.get_dfg_graph(dataframe, measure="performance")
    activities_count = attributes_filter.get_attribute_values(dataframe, xes.DEFAULT_NAME_KEY)
    gviz = dfg_vis_factory.apply(dfg, activities_count=activities_count, variant="performance", parameters={"format": "svg"})
    return get_base64_from_gviz(gviz)