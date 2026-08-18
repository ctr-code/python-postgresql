import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# cursor.execute("select * from artist;")
# cursor.execute("select name from artist;")
# cursor.execute("select * from artist where name=%s", ["Queen"])
# cursor.execute("select * from artist where artist_id=%s", [51])
# cursor.execute("select * from album where artist_id=%s", [51])
cursor.execute("select * from track where composer=%s", ["Queen"])

# Fetch many results
results = cursor.fetchall()

# Fetch exactly one result
# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)
