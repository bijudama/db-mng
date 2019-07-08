import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="159753", host="127.0.0.1", port="5432")
cursor = con.cursor()
print("Database opened successfully")