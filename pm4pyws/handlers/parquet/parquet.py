from pm4py.objects.log.importer.parquet import factory as parquet_importer

from pm4pyws.handlers.parquet.process_schema import factory as process_schema_factory


class ParquetHandler(object):
    def __init__(self, path):
        self.dataframe = parquet_importer.apply(path)

    def get_schema(self, variant=process_schema_factory.DFG_FREQ, parameters=None):
        return process_schema_factory.apply(self.dataframe, variant=variant, parameters=parameters)
