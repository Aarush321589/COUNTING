# Program to count digits using a while loop

# Get input from user
number = input("Enter a number: ")

# Make sure it's a valid number (handling negative sign)
if number.startswith('-'):
    number = number[1:]

# Convert to integer
num = int(number)

# Initialize digit counter
count = 0

# Special case for 0
if num == 0:
    count = 1
else:
    # Count digits using while loop
    while num > 0:
        num //= 10
        count += 1

# Output the result
print("Total number of digits:", count)
W