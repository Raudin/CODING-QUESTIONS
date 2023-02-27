# Function to convert decimal to binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# Taking input from user
decimal = int(input("Enter a decimal number: "))

# Printing the binary equivalent
print("The binary equivalent of", decimal, "is", decimal_to_binary(decimal))