# Python program demonstrating type casting

# Original values
original_int = 42
original_float = 3.14
original_string = "123"

# Type casting examples

# int to float
int_to_float = float(original_int)
print(f"Original int: {original_int} (type: {type(original_int)})")
print(f"Converted to float: {int_to_float} (type: {type(int_to_float)})")

# float to int
float_to_int = int(original_float)
print(f"Original float: {original_float} (type: {type(original_float)})")
print(f"Converted to int: {float_to_int} (type: {type(float_to_int)})")

# int to string
int_to_string = str(original_int)
print(f"Original int: {original_int} (type: {type(original_int)})")
print(f"Converted to string: {int_to_string} (type: {type(int_to_string)})")

# Additional examples
# string to int
string_to_int = int(original_string)
print(f"Original string: {original_string} (type: {type(original_string)})")
print(f"Converted to int: {string_to_int} (type: {type(string_to_int)})")

# string to float
string_to_float = float(original_string)
print(f"Original string: {original_string} (type: {type(original_string)})")
print(f"Converted to float: {string_to_float} (type: {type(string_to_float)})")

# float to string
float_to_string = str(original_float)
print(f"Original float: {original_float} (type: {type(original_float)})")
print(f"Converted to string: {float_to_string} (type: {type(float_to_string)})")