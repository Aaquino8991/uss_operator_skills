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
ipdb.set_trace()