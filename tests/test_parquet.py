import os
import unittest

from pm4pyws.handlers.parquet.parquet import ParquetHandler


def do_log(path):
    handler = ParquetHandler()
    handler.build_from_path(path)
    handler.get_schema(variant="dfg_freq")
    handler.get_schema(variant="dfg_perf")
    handler.get_schema(variant="inductive_freq")
    handler.get_schema(variant="inductive_perf")
    handler.get_schema(variant="indbpmn_freq")
    handler.get_schema(variant="indbpmn_perf")
    handler.get_schema(variant="heuristics_freq")
    handler.get_schema(variant="heuristics_perf")
    handler.get_schema(variant="tree_freq")
    handler.get_schema(variant="tree_perf")
    handler.get_case_duration_svg()
    handler.get_events_per_time_svg()
    handler.get_sna(variant="handover")
    handler.get_sna(variant="working_together")
    handler.get_sna(variant="subcontracting")
    handler.get_sna(variant="jointactivities")
    handler.get_transient(86400)

class ParquetTests(unittest.TestCase):
    def test_parquets(self):
        do_log("logs//running-example.parquet")
        do_log("logs//receipt.parquet")


if __name__ == "__main__":
    unittest.main()
