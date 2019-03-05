from pm4py.objects.log.importer.parquet import factory as parquet_importer

from pm4pyws.handlers.parquet.process_schema import factory as process_schema_factory
from pm4pyws.handlers.parquet.statistics import case_duration, events_per_time


class ParquetHandler(object):
    def __init__(self, path):
        self.dataframe = parquet_importer.apply(path)

    def get_schema(self, variant=process_schema_factory.DFG_FREQ, parameters=None):
        return process_schema_factory.apply(self.dataframe, variant=variant, parameters=parameters)

    def get_case_duration_svg(self, parameters=None):
        return case_duration.get_case_duration_svg(self.dataframe, parameters=parameters)

    def get_events_per_time_svg(self, parameters=None):
        return events_per_time.get_events_per_time_svg(self.dataframe, parameters=parameters)
