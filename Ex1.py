# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:26:13 2023

@author: Karin Sofi
"""

x1 = "a"
x2 = -2.0
x3 = 0.0


def my_func(x1, x2, x3):
    if isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float) == True:
        xT = (x1 + x2 + x3)
        up = xT * (x2 + x3) * x3
        if xT == 0:
            return 'Not a number – denominator equals zero'
        else:
            return (up / xT)
    elif isinstance(x1, int) and isinstance(x2, int) and isinstance(x3, int) == True:
        return 'Error: parameters should be float'
    else:
        return 'None'


x = my_func(x1, x2, x3)
print(x)

