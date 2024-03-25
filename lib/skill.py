from __init__ import CURSOR, CONN

class Skill:

    def __init__(self, skill_name):
        self.id = id
        self.skill_name = skill_name

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY,
            skill_name TEXT
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