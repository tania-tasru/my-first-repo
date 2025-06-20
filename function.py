# Function
def propose():
    print("You will be the moon of my sky.")
    print("We will sail through the ocean of happiness.")
propose()

# Function Parameter
def add_20(num):
    result = num + 20
    print(result)
add_20(21)

def add_numbers(a, b):
    total = a + b
    print(total)
add_numbers(10, 6)

def multiply_numbers(a, b, c):
    result = a * b * c
    print(result)
multiply_numbers(5, 7, 9)

def subtraction_numbers(x, y, z):
    result = x - y - z
    print(result)
subtraction_numbers(9, 7, 2)

# Return
def get_expense(tuition, rent):
    total = tuition + rent
    return total
print(get_expense(5000, 1500))

def add(x, y):
    return x + y
a = add(5, 6)
b = add(2, 4)
c = add(a, b)
print(c)

# Is odd
def is_odd(num):
    return num % 2 != 0
print(is_odd(30))

# Evenify
def is_odd(num):
    return num % 2 != 0

def evenify(num):
    if is_odd(num):
        even_number = num * 2
    else:
        even_number = num
    return even_number

result = evenify(5)
print(result)