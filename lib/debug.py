#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from employee import Employee
from skill import Skill

import ipdb

def reset_database():
    Employee.drop_table()
    Employee.create_table()

    Skill.drop_table()
    Skill.create_table()

reset_database()

anthony = Employee.add_employee("Anthony", 34)

anthony.name = "Tony"
anthony.age = 35
anthony.update()

liset = Employee.add_employee("Liset", 32)

liset.delete()

ipdb.set_trace()