from __init__ import CURSOR, CONN

class Factory:

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