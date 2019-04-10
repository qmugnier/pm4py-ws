import sqlite3
conn = sqlite3.connect('event_logs.db')
c = conn.cursor()

c.execute("CREATE TABLE EVENT_LOGS(LOG_NAME PRIMARY KEY, LOG_PATH)")
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("running-example(xes)","logs/running-example.xes"))
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("receipt(xes)","logs/receipt.xes"))
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("running-example","logs/running-example.parquet"))
c.execute("INSERT INTO EVENT_LOGS VALUES (?,?)",("receipt","logs/receipt.parquet"))

c.execute("CREATE TABLE ADMINS(USER_ID PRIMARY KEY)")
c.execute("INSERT INTO ADMINS VALUES ('admin')")

c.execute("CREATE TABLE USER_LOG_VISIBILITY(USER_ID, LOG_NAME)")
c.execute("INSERT INTO USER_LOG_VISIBILITY VALUES ('user1', 'running-example')")
c.execute("INSERT INTO USER_LOG_VISIBILITY VALUES ('user2', 'receipt')")

c.execute("CREATE TABLE USER_LOG_DOWNLOADABLE(USER_ID, LOG_NAME)")
c.execute("INSERT INTO USER_LOG_DOWNLOADABLE VALUES ('user1', 'running-example')")

c.execute("CREATE TABLE USER_UPLOADABLE(USER_ID PRIMARY KEY)")
c.execute("INSERT INTO USER_UPLOADABLE VALUES ('user1')")

conn.commit()