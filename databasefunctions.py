import sqlite3

# Database connection
def create_database_connection():
    return sqlite3.connect('my_database.db')

def insert_data_into_database(data):
    try:
        conn = create_database_connection()
        cursor = conn.cursor()

        # Customize the SQL statement based on your schema and data format
        cursor.execute("INSERT INTO Machines (hostname, ip_address, uptime, mac_address) VALUES (?, ?, ?, ?)",
                       (data["hostname"], data["ip_address"], data["uptime"], data['mac_address']))

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error inserting data into the database: {str(e)}")