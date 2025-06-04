# Calculations.py
# This file contains basic math operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def AbdoDivide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
