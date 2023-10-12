import pymysql
host = 'ENMA'
user = 'root'
password = ''
database = 'student'
connection = pymysql.connect(host=host, user=user, password=password, database=database)

try:
    with connection.cursor() as cursor:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
        """
        cursor.execute(create_table_query)
        insert_records_query = """
        INSERT INTO example_table (name, age) VALUES
        ('santhosh', 20),
        ('suriya', 20),
        ('arjun', 22)
        """
        cursor.execute(insert_records_query)
    connection.commit()

    print("Table created and records inserted successfully!")

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    connection.close()