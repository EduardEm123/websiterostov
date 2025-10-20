def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

def power(a,b):
    return a ** b

def factorial(a):
    num = 1
    for i in range(2, a + 1):
        num *=i
    return num

def is_even(a):
    even = 'Четное'
    odd = 'Нечетное'
    if a % 2 == 0:
        return even
    else:
        return odd