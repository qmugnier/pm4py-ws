from pm4py.algo.conformance.alignments import factory as align_factory
from pm4py.objects.petri.common import final_marking
from pm4py.objects.petri.common import initial_marking
from pm4py.objects.petri.importer.versions import pnml
from pm4py.visualization.align_table import factory as align_table_factory
from pm4py.visualization.common.utils import get_base64_from_gviz
from pm4py.visualization.petrinet import factory as pn_vis_factory
from pm4py.visualization.petrinet.util import alignments_decoration


def perform_alignments(log, petri_string, parameters=None):
    """
    Perform alignments

    Parameters
    ------------
    log
        Log
    net
        Petri net
    parameters
        Parameters of the algorithm

    Returns
    -------------
    petri
        SVG of the decorated Petri
    table
        SVG of the decorated table
    """
    if parameters is None:
        parameters = {}

    net, im, fm = pnml.import_petri_from_string(petri_string, parameters=parameters)

    alignments = align_factory.apply(log, net, im, fm, parameters={"ret_tuple_as_trans_desc": True})
    decorations = alignments_decoration.get_alignments_decoration(net, im, fm, aligned_traces=alignments)

    gviz_on_petri = pn_vis_factory.apply(net, im, fm, aggregated_statistics=decorations, variant="alignments", parameters={"format": "svg"})
    svg_on_petri = get_base64_from_gviz(gviz_on_petri)

    gviz_table = align_table_factory.apply(log, alignments, parameters={"format": "svg"})
    svg_table = get_base64_from_gviz(gviz_table)

    return svg_on_petri, svg_table
