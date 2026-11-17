"""
#https://github.com/AngelicaV-L/lab11-AV-RF
#Partner 1: Angelica Velazquez-Lassalle
#Parter 2: Robert F

calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def square_root (a) :
    if a < 0:
        raise ValueError
    math.sqrt(a)

def hypotenuse(a,b):
    math.hypot(a,b)

def add(a, b): return a + b

def subtract(a,b): return a - b

def multiply (a,b): return a * b

def exponent(a,b): return a**b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def logarithm(a,b):

    if b == 0:
        raise ValueError
    else:
        logarithm(b,a)

def exp(a,b):
    return a ** b