#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from employee import Employee
from skill import Skill



def reset_database():
    Employee.drop_table()
    Employee.create_table()

    Skill.drop_table()
    Skill.create_table()

reset_database()

anthony = Employee.add_employee("Anthony", 34)
liset = Employee.add_employee("Liset", 32)
fernan = Employee.add_employee("Fernan", 31)
michelle = Employee.add_employee("Michelle", 29)

import ipdb; ipdb.set_trace()