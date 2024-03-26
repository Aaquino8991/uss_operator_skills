from __init__ import CURSOR, CONN

class Employee:

    all = {}

    def __init__(self, name, age, factory_id, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.factory_id = factory_id

    def __repr__(self):
        return f"<Employee {self.id}: {self.name}, {self.age}>"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            factory_id INTEGER,
            FOREIGN KEY (factory_id) REFERENCES factories(id)
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
            INSERT INTO employees (name, age, factory_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.factory_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def add_employee(cls, name , age, factory_id):
        employee = cls(name, age, factory_id)
        employee.save()
        return employee
    
    def update(self):
        sql = """
            UPDATE employees
            SET name = ?, age = ?, factory_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.age, self.factory_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        employee = cls.all.get(row[0])
        if employee:
            employee.name = row[1]
            employee.age = row[2]
            employee.factory_id = row[3]
        else:
            employee = cls(row[1], row[2], row[3])
            employee.id = row[0]
            cls.all[employee.id] = employee
        return employee
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM employees
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM employees
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM employees
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    






    # Mapping Object Relationships 
    # Updating Employee class to store the relationship with Factory class.