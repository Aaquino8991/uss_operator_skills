from __init__ import CURSOR, CONN

class Factory:

    all = {}

    def __init__(self, factory_name, location, factory_id=None):
        self.factory_id = factory_id
        self.factory_name = factory_name
        self.location = location

    def __repr__(self):
        return f'<Factory {self.factory_id}: {self.factory_name}>'
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS factories (
            factory_id INTEGER PRIMARY KEY,
            factory_name TEXT,
            location TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS factories
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO factories(factory_name, location)
            VALUES ?, ?
        """

        CURSOR.execute(sql, (self.factory_name, self.location))
        CONN.commit()

        self.factory_id = CURSOR.lastrowid
        type(self).all[self.factory_id] = self

    @classmethod
    def create_factory(cls, factory_name, location):
        factory = cls(factory_name, location)
        factory.save()
        return factory

    def update(self):
        sql = """
            UPDATE factories
            SET factory_name = ?, location = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.factory_name, self.location))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM factories
            WHERE factory_id = ?
        """

        CURSOR.execute(sql, (self.factory_id,))
        CONN.commit()

        del type(self).all[self.factory_id]
        self.factory_id = None

    @classmethod
    def instance_from_db(cls, row):
        factory = cls.all.get(row[0])
        if factory:
            factory.name = row[1]
            factory.age = row[2]
            factory.factory_id = row[3]
        else:
            factory = cls(row[1], row[2], row[3])
            factory.id = row[0]
            cls.all[factory.factory_id] = factory
        return factory
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM factories
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, factory_id):
        sql = """
            SELECT *
            FROM factories
            WHERE factory_id = ?
        """

        row = CURSOR.execute(sql, (factory_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, factory_name):
        sql = """
            SELECT *
            FROM factories
            WHERE factory_name is ?
        """

        row = CURSOR.execute(sql, (factory_name,)).fetchone()
        return cls.instance_from_db(row) if row else None