from __init__ import CURSOR, CONN

class Employee:

    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Employee {self.id}: {self.name}>"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employees
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO employees (name, skills)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.skills))
        CONN.commit()

        self.id = CURSOR.lastrowid