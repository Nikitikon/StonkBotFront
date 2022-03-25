import psycopg2

conn = psycopg2.connect(dbname='myusers', user='userscontroller',
                        password='1912', host='localhost')
cursor = conn.cursor()



cursor.close()
conn.close()

