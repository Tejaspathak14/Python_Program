# Python program demonstrating string operations

# Take input from the user
user_input = input("Enter a string: ")

print(f"Original string: '{user_input}'")
print(f"Length of string: {len(user_input)}")
print()

# String concatenation
additional_text = " is awesome!"
concatenated = user_input + additional_text
print(f"Concatenated string: '{concatenated}'")
print()

# String indexing
if len(user_input) > 0:
    print(f"First character: '{user_input[0]}'")
    print(f"Last character: '{user_input[-1]}'")
    if len(user_input) > 1:
        print(f"Second character: '{user_input[1]}'")
print()

# String slicing
if len(user_input) >= 3:
    print(f"First 3 characters: '{user_input[:3]}'")
    print(f"Last 3 characters: '{user_input[-3:]}'")
    print(f"Characters from index 1 to 3: '{user_input[1:4]}'")
else:
    print("String is too short for slicing examples.")
print()

# String methods
print("String methods:")
print(f"Uppercase: '{user_input.upper()}'")
print(f"Lowercase: '{user_input.lower()}'")
print(f"Title case: '{user_input.title()}'")
print()

# Split method
words = user_input.split()
print(f"Split into words: {words}")
print()

# Replace method
replaced = user_input.replace("a", "@").replace("e", "3")
print(f"Replaced 'a' with '@' and 'e' with '3': '{replaced}'")
print()

# Check if string contains a substring
if "python" in user_input.lower():
    print("The string contains 'python' (case-insensitive).")
else:
    print("The string does not contain 'python'.")