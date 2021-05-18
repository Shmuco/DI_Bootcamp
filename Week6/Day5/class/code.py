import psycopg2
import psycopg2.extras


HOSTNAME = '127.0.0.1'
USERNAME = ''
PASSWORD = 'password'
DATABASE = 'Hollywood'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

query = "SELECT  first_name, last_name FROM actors;"

cursor.execute(query)
results = cursor.fetchall()

print(results)