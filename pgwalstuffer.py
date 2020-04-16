import time
import psycopg2

SQL_CREATE_TABLE="CREATE TABLE IF NOT EXISTS walstuffer (id int);"

conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="postgres")

cur = conn.cursor()
        
print('PostgreSQL database version:')
cur.execute('SELECT version()')

print(cur.fetchone())

cur = conn.cursor()
cur.execute(SQL_CREATE_TABLE)
conn.commit()

while True:
	epoch=str(int(time.time()))

	SQL_INSERT="insert into walstuffer values ("+epoch+");"

	cur.execute(SQL_INSERT)
	conn.commit()
	print(SQL_INSERT)
	
	time.sleep(5)
