#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from employee import Employee
from skill import Skill
from factory import Factory



def reset_database():
    Employee.drop_table()
    Employee.create_table()

    Skill.drop_table()
    Skill.create_table()

    Factory.drop_table()
    Factory.create_table()

reset_database()

anthony = Employee.add_employee("Anthony", 34, 1)
liset = Employee.add_employee("Liset", 32, 2)
fernan = Employee.add_employee("Fernan", 31, 1)
michelle = Employee.add_employee("Michelle", 29, 3)

ace = Factory.add_factory("Ace", "Building 1")
michigan = Factory.add_factory("Michigan", "Building 2")
fontana = Factory.add_factory("Fontana", "Building 3")

import ipdb; ipdb.set_trace()