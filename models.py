import sqlite3


def drop_table():
    with sqlite3.connect('environment.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS environment""")
    return True


def create_db():
    with sqlite3.connect('environment.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE environment(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property TEXT NOT NULL,
            measurement INTEGER NOT NULL,
            status TEXT NOT NULL
        );
        """
        c.execute(table)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
