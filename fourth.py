# Python program demonstrating arithmetic, comparison, and logical operations

# Define two numbers
a = 10
b = 3

print(f"Numbers: a = {a}, b = {b}")
print()

# Arithmetic operations
print("Arithmetic Operations:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division (float)
print(f"a // b = {a // b}")  # Floor division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation
print()

# Comparison operations
print("Comparison Operations:")
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a < b: {a < b}")  # Less than
print(f"a > b: {a > b}")  # Greater than
print(f"a <= b: {a <= b}")  # Less than or equal to
print(f"a >= b: {a >= b}")  # Greater than or equal to
print()

# Logical operations (using boolean results from comparisons)
print("Logical Operations:")
x = a > b  # True
y = a < b  # False
print(f"x = (a > b) = {x}")
print(f"y = (a < b) = {y}")
print(f"x and y: {x and y}")  # Logical AND
print(f"x or y: {x or y}")  # Logical OR
print(f"not x: {not x}")  # Logical NOT
print(f"not y: {not y}")  # Logical NOT