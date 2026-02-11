import MySQLdb

config = {
    'user': 'root',
    'passwd': 'root',
    'host': 'localhost',
}

try:
    print("Connecting to MySQL...")
    db = MySQLdb.connect(**config)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_db DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
    print("Database 'hospital_db' created successfully.")
except Exception as e:
    print(f"Error creating database: {e}")
finally:
    if 'db' in locals():
        db.close()
