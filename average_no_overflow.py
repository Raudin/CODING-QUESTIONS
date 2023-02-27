# Take two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compute the average
average = (num1 / 2) + (num2 / 2) + ((num1 % 2 + num2 % 2) / 2)

# Print the average
print("The average of", num1, "and", num2, "is", average)