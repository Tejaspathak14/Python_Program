# Python program to determine student result based on marks

# Function to get valid marks input
def get_marks():
    while True:
        try:
            marks = int(input("Enter the student's marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get marks from user
marks = get_marks()

# Determine result using conditional statements
if marks >= 60:
    result = "Pass"
    message = "Congratulations! You have passed."
elif marks >= 40:
    result = "Eligible for Re-test"
    message = "You are eligible for a re-test. Better luck next time!"
else:
    result = "Fail"
    message = "Unfortunately, you have failed. Please try again."

# Display the result
print(f"\nMarks: {marks}")
print(f"Result: {result}")
print(message)