import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="password"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT 1 + 1")

# Fetch the results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
