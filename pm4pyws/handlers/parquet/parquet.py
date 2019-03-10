from pm4py.algo.filtering.common.filtering_constants import CASE_CONCEPT_NAME
from pm4py.objects.log.adapters.pandas import csv_import_adapter
from pm4py.objects.log.importer.parquet import factory as parquet_importer
from pm4py.objects.log.util import xes
from pm4py.statistics.traces.pandas import case_statistics
from pm4py.util import constants

from pm4pyws.handlers.parquet.cases import variants
from pm4pyws.handlers.parquet.process_schema import factory as process_schema_factory
from pm4pyws.handlers.parquet.sna import get_sna as sna_obtainer
from pm4pyws.handlers.parquet.statistics import case_duration, events_per_time


class ParquetHandler(object):
    def __init__(self):
        self.dataframe = None
        self.first_ancestor = None
        self.last_ancestor = None
        self.variants_df = None

    def build_from_path(self, path, parameters=None):
        if parameters is None:
            parameters = {}
        self.dataframe = parquet_importer.apply(path)
        self.build_variants_df()

    def build_from_csv(self, path, parameters=None):
        if parameters is None:
            parameters = {}
        activity_key = parameters[
            constants.PARAMETER_CONSTANT_ACTIVITY_KEY] if constants.PARAMETER_CONSTANT_ACTIVITY_KEY in parameters else xes.DEFAULT_NAME_KEY
        timestamp_key = parameters[
            constants.PARAMETER_CONSTANT_TIMESTAMP_KEY] if constants.PARAMETER_CONSTANT_TIMESTAMP_KEY in parameters else xes.DEFAULT_TIMESTAMP_KEY
        case_id_glue = parameters[
            constants.PARAMETER_CONSTANT_CASEID_KEY] if constants.PARAMETER_CONSTANT_CASEID_KEY in parameters else CASE_CONCEPT_NAME

        self.dataframe = csv_import_adapter.import_dataframe_from_path(path)
        if not activity_key == xes.DEFAULT_NAME_KEY:
            self.dataframe[xes.DEFAULT_NAME_KEY] = activity_key
        if not timestamp_key == xes.DEFAULT_TIMESTAMP_KEY:
            self.dataframe[xes.DEFAULT_TIMESTAMP_KEY] = timestamp_key
        if not case_id_glue == CASE_CONCEPT_NAME:
            self.dataframe[case_id_glue] = CASE_CONCEPT_NAME
        self.build_variants_df()

    def build_variants_df(self, parameters=None):
        self.variants_df = case_statistics.get_variants_df(self.dataframe, parameters=parameters)

    def get_schema(self, variant=process_schema_factory.DFG_FREQ, parameters=None):
        return process_schema_factory.apply(self.dataframe, variant=variant, parameters=parameters)

    def get_case_duration_svg(self, parameters=None):
        return case_duration.get_case_duration_svg(self.dataframe, parameters=parameters)

    def get_events_per_time_svg(self, parameters=None):
        return events_per_time.get_events_per_time_svg(self.dataframe, parameters=parameters)

    def get_variant_statistics(self, parameters=None):
        if parameters is None:
            parameters = {}
        parameters["variants_df"] = self.variants_df

        return variants.get_statistics(self.dataframe, parameters=parameters)

    def get_sna(self, variant="handover", parameters=None):
        return sna_obtainer.apply(self.dataframe, variant=variant, parameters=parameters)
