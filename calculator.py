# https://github.com/newmanhw/lab10-swe
# Partner 1: Isabel Sanchez
# Partner 2: Moline Charles

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as err:
        raise err
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as err:
        raise err
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def log(a, b):
    if a <= 0 or a == 1 or b <=0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b

'''
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    return math.log(a, b)

def exp(a, b):
    return a ** b

'''
