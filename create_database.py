import sqlite3
conn = sqlite3.connect('event_logs.db')
c = conn.cursor()

c.execute("CREATE TABLE EVENT_LOGS(LOG_NAME PRIMARY KEY, LOG_PATH)")
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("running-example(xes)","logs/running-example.xes"))
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("receipt(xes)","logs/receipt.xes"))
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("running-example","logs/running-example.parquet"))
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("receipt","logs/receipt.parquet"))

conn.commit()