# Python program to check if a number is even or odd

# Function to get valid integer input
def get_number():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Get number from user
number = get_number()

# Check if even or odd using relational operator
if number % 2 == 0:
    result = "even"
    message = "The number is even."
else:
    result = "odd"
    message = "The number is odd."

# Display the result
print(f"\nNumber: {number}")
print(f"It is {result}.")
print(message)

# Additional check using logical operators (for demonstration)
is_even = (number % 2 == 0) and True
is_odd = (number % 2 != 0) or False

print(f"\nUsing logical operators:")
print(f"Is even: {is_even}")
print(f"Is odd: {is_odd}")