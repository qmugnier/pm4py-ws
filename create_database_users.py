import sqlite3
conn_users = sqlite3.connect('users.db')
curs_users = conn_users.cursor()

curs_users.execute("CREATE TABLE USERS(USER_ID PRIMARY KEY, PASSWORD)")
curs_users.execute("INSERT INTO USERS VALUES (?,?)",('admin', 'admin'))

curs_users.execute("CREATE TABLE SESSIONS(SESSION_ID PRIMARY KEY, USER_ID, CREATION_DATE)")

conn_users.commit()