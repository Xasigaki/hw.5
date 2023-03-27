
import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH/DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        price INTEGER,
        photo TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        username TEXT,
        address TEXT,
        FOREIGN KEY (product_id)
            REFERENCES products(id)
            ON DELETE CASCADE
    )
    """)

    db.commit()


def add_clients(data):
    data = data.as_dict()
    cursor.execute("""INSERT INTO orders(product_id,username,address) VALUES 
    (:username,:address,:product_id)""",
                {'username': data['username2'],
                'address': data['address2'],
                'product_id': data['product_id']})

    db.commit()

def add_products():
    cursor.execute("""INSERT INTO products(name, description, price, photo) VALUES 
    ('Тонкое искусство пофигизма', 'Книга для саморазвития!',100, '/images/1.jpeg'),
    ('Поток', 'Книга для саморазвития!', 200, '/images/2.png')
    """)

    db.commit()

def delete_table_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


def get_products():
    cursor.execute("""
    SELECT * FROM products;
    """)

    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    delete_table_products()
    create_tables()
    add_clients()
    add_products()