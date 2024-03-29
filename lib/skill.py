from __init__ import CURSOR, CONN


class Skill:

    all = {}

    def __init__(self, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Skill {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS skills
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO skills (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def add_skill(cls, name):
        skill = cls(name)
        skill.save()
        return skill
    
    def update(self):
        sql = """
            UPDATE skills
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM skills
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):

        skill = cls.all.get(row[0])
        if skill:
            skill.name = row[1]
        else:
            skill = cls(row[1])
            skill.id = row[0]
            cls,all[skill.id] = skill
        return skill
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM skills
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM skills
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM skills
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def employees(self):
        from employee import Employee
        sql = """
            SELECT * FROM employees
            WHERE skills_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Employee.instance_from_db(row) for row in rows
        ]
    
    def list_employees(self):
        from employee import Employee
        return [employee for employee in Employee.all if self in str(employee.skills())]
    
    def add_employee(self, employee):
        from employee import Employee
        if isinstance(employee, Employee):
            employee.add_skill(self)
        else:
            raise ValueError("Employee not found.")