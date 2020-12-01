# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:55:25 2020

@author: BINIT KUMAR
"""

import random

lower="abcdefghijklmnopqrstvvwzyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,_-"

all=lower+upper+numbers+symbols

length=16
password="".join(random.sample(all,length))
print(password)