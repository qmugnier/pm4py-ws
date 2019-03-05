from pm4pyws import main_service


def load_logs():
    main_service.load_log("roadtraffic", "C:\\receipt.parquet")


if __name__ == "__main__":
    load_logs()
    app = main_service.app
    app.run(host="0.0.0.0", port="5000", threaded=True)
