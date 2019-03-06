from pm4py.statistics.traces.pandas import case_statistics


def get_statistics(df, parameters=None):
    if parameters is None:
        parameters = {}

    variants_statistics = case_statistics.get_variant_statistics(df)

    return variants_statistics
