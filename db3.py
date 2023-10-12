import pymysql
host = 'ENMA'
user = 'root'
password = ''
database = 'student'
connection = pymysql.connect(host=host, user=user, password=password, database=database)

try:
    option=int(input("enter the option?"))
    with connection.cursor() as cursor:

        if option == 1:
            create_table_query = """
             CREATE TABLE IF NOT EXISTS example_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                 age INT
             )
            """
            cursor.execute(create_table_query)
            print("Table created successfully!")
        elif option == 2:
            insert_records_query = """
            INSERT INTO example_table (name, age) VALUES
             ('santhosh', 20),
             ('suriya', 20),
             ('arjun', 22)
             """
            cursor.execute(insert_records_query)
            print("Records inserted successfully!")
        elif option == 3:
            create1_table_query = """
            alter table example_table add(gender varchar(4))
            """
            cursor.execute(create1_table_query)
            print("Table altered successfully!")
        elif option == 4:
            update_record_query="""
            update example_table
            set gender = 'm'
            where age = 20
            """
            cursor.execute(update_record_query)
            print("Table updated successfully")
        elif option == 5:
            select_query= """
            select * from example_table
            """
            cursor.execute(select_query)
            print(example_table)
        else:
            print("Invalid option")

   

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    connection.close()