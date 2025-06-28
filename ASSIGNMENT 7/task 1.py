import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="5433", host="localhost", port=5432)
    cursor = conn.cursor()
    cursor.execute('''create table employees (name TEXT, id INT , age int);
    ''')
    print("Table created successfully")
    conn.commit()
    conn.close()
table()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="5433", host="localhost", port=5432)
    cursor = conn.cursor()

    name = input("enter name: ")
    id = input("enter id: ")
    age = input("enter roll: ")
   

    query = '''insert into employees(name, id, age) VALUES (%s, %s, %s, %s, %s);'''
    cursor.execute(query, (name, id, age))

    # cursor.execute(''' insert into employees(name, id, age) VALUES ('sam',01,30) ''')

    print("Data added successfully")
    conn.commit()
    conn.close()
data()

def extract():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="5433",host="localhost",port=5432 )
    cursor = conn.cursor()
    cursor.execute('select * from employees;')
    print(cursor.fetchone())  
    conn.commit()
    conn.close()
extract()
