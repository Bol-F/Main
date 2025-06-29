import sqlite3
import psycopg2


class SQLManager:
    def __init__(self, db_name='sqlite.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            self.conn.close()


class POSManager:
    def __init__(self, dbname='postgres', user='postgres', password='2006.08.10.bol', host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            self.conn.close()


# Create PostgreSQL table if not exists
with POSManager() as pos:
    pos.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            firstname VARCHAR(50),
            lastname VARCHAR(50),
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("PostgreSQL table ensured")

# Create SQLite table if not exists
with SQLManager() as sql:
    sql.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE,
            firstname VARCHAR(50),
            lastname VARCHAR(50),
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("SQLite table ensured")


class Users:
    def __init__(self, username, firstname, lastname, age, id=None):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.id = id

    def add_user_sqlite(self):
        with SQLManager() as sql:
            sql.execute(
                """INSERT INTO users(username, firstname, lastname, age) VALUES (?, ?, ?, ?)""",
                (self.username, self.firstname, self.lastname, self.age)
            )
            self.id = sql.lastrowid
            print(f"SQLite: Added user with ID {self.id}")

    def add_user_postgres(self):
        try:
            with POSManager() as pos:
                pos.execute(
                    """INSERT INTO users(username, firstname, lastname, age) VALUES (%s, %s, %s, %s) RETURNING id""",
                    (self.username, self.firstname, self.lastname, self.age)
                )
                self.id = pos.fetchone()[0]
                print(f"PostgreSQL: Added user with ID {self.id}")
        except Exception as e:
            print(f"PostgreSQL error: {e}")

    def get_by_id_sqlite(self, user_id):
        with SQLManager() as sql:
            sql.execute("""SELECT * FROM users WHERE id = ?""", (user_id,))
            return sql.fetchone()

    def get_by_id_postgres(self, user_id):
        with POSManager() as pos:
            pos.execute("""SELECT * FROM users WHERE id = %s""", (user_id,))
            return pos.fetchone()


# Only run tests if we're executing directly
if __name__ == "__main__":
    # Test PostgreSQL
    print("\nTesting PostgreSQL:")
    postgres_user = Users("pg_user", "Alice", "Smith", 25)
    postgres_user.add_user_postgres()

    # Get and print the user
    user_data = postgres_user.get_by_id_postgres(postgres_user.id)
    print(f"Retrieved PostgreSQL user: {user_data}")

    # Test SQLite
    print("\nTesting SQLite:")
    sqlite_user = Users("sqliatfe_user", "John", "Doe", 30)
    sqlite_user.add_user_sqlite()

    # Get and print the user
    user_data = sqlite_user.get_by_id_sqlite(sqlite_user.id)
    print(f"Retrieved SQLite user: {user_data}")