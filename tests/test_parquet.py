import os
import unittest

from pm4pyws.handlers.parquet.parquet import ParquetHandler


class ParquetTests(unittest.TestCase):
    def test_parquets(self):
        handler = ParquetHandler()
        handler.build_from_path("logs//running-example.parquet")
        handler.get_schema(variant="dfg_freq")
        handler.get_schema(variant="dfg_perf")
        handler.get_schema(variant="inductive_freq")
        handler.get_schema(variant="inductive_perf")
        handler.get_schema(variant="tree_freq")
        handler.get_schema(variant="tree_perf")
        handler.get_case_duration_svg()
        handler.get_events_per_time_svg()
        handler.get_sna(variant="handover")
        handler.get_sna(variant="working_together")
        handler.get_sna(variant="subcontracting")
        handler.get_sna(variant="jointactivities")
        handler.get_transient(86400)


if __name__ == "__main__":
    unittest.main()
