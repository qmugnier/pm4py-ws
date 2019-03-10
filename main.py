from pm4pyws.entrypoint import PM4PyServices

S = PM4PyServices()
S.load_log("receipt", "receipt.parquet")
S.serve()