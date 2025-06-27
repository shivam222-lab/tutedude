import psycopg2

def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="5433", host="localhost", port=5432)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS student (name TEXT, id INT,roll INT,email TEXT,phone BIGINT);
    ''')
    print("Table created successfully")
    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="5433", host="localhost", port=5432)
    cursor = conn.cursor()

    name = input("enter name: ")
    id = input("enter id: ")
    roll = input("enter roll: ")
    email = input("enter email: ")
    phone = input("enter phone: ")

    query = '''INSERT INTO student(name, id, roll, email, phone) VALUES (%s, %s, %s, %s, %s);'''
    cursor.execute(query, (name, id, roll, email, phone))

    print("Data added successfully")
    conn.commit()
    conn.close()

def extract():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="5433",host="localhost",port=5432 )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student;')
    print(cursor.fetchone())  
    conn.commit()
    conn.close()


table()
data()
extract()