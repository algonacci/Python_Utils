import mysql.connector

def test_mysql_connection(host, user, password, database):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Check if the connection was successful
        if conn.is_connected():
            print("Connected to MySQL database")

            # Create a cursor to execute SQL queries
            cursor = conn.cursor()

            # Execute the SHOW DATABASES query
            cursor.execute("SHOW DATABASES;")

            # Fetch all the rows returned by the query
            databases = cursor.fetchall()

            # Print the list of databases
            print("Databases:")
            for db in databases:
                print(db[0])

            # Close the cursor and connection
            cursor.close()
            conn.close()

        else:
            print("Failed to connect to MySQL database")

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

# Replace the following values with your MySQL connection details
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

# Call the function to test the MySQL connection
test_mysql_connection(host, user, password, database)

