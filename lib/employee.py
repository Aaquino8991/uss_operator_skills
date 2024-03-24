from __init__ import CURSOR, CONN

class Employee:

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Employee {self.id}: {self.name}>"
    
    