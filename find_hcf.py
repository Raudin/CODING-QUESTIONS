# Function to find HCF of two numbers
def find_hcf(num1, num2):
    # Using Euclidean algorithm
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Printing the HCF
print("The HCF of", num1, "and", num2, "is", find_hcf(num1, num2))