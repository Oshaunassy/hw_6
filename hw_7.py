import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product_title(conn, product_title):
    sql = '''INSERT INTO products
    (product_title, quantity, price)
    VALUES(?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product_title)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_title(conn, product_title):
    sql = '''UPDATE products SET quantity = ?, price = ?
            WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product_title)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product_title(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quantity(conn, price, quantity):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price, quantity))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)

def select_products_by_product_title(conn, product_title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_title,))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)

connection = create_connection('hw.db')

if connection is not None:
    print('Successfully connected!')
    sql_create_products_table = '''
    CREATE TABLE products (
    id integer primary key autoincrement,
    product_title VARCHAR (200) NOT NULL,
    quantity FLOAT NOT NULL DEFAULT 0.00,
    price FLOAT ROUND(10),2 NOT NULL DEFAULT 0.00
)
'''
    # create_table(connection, sql_create_products_table)
    # insert_product_title(connection, ('Bread', 515, 25))
    # insert_product_title(connection, ('Sugar', 1000, 87))
    # insert_product_title(connection, ('Rice', 500, 65))
    # insert_product_title(connection, ('Butter', 200, 115))
    # insert_product_title(connection, ('Cheese', 200, 105))
    # insert_product_title(connection, ('Buckwheat', 300, 120))
    # insert_product_title(connection, ('Pasta', 100, 70))
    # insert_product_title(connection, ('Beef', 750, 500))
    # insert_product_title(connection, ('Chicken beef', 550, 350))
    # insert_product_title(connection, ('Flour', 3050, 35))
    # insert_product_title(connection, ('Milk', 250, 68))
    # insert_product_title(connection, ('Sausages', 350, 497))
    # insert_product_title(connection, ('Fish', 250, 2000))
    # insert_product_title(connection, ('Juice', 250, 115))
    # insert_product_title(connection, ('Cigarette', 600, 200))
    # update_product_title(connection, (800, 85, 2))
    # delete_product_title(connection, 5)
    # select_all_products(connection)
    # select_products_by_price_and_quantity(connection, 100, 500)
    select_products_by_product_title(connection, 'rice')

    connection.close()
