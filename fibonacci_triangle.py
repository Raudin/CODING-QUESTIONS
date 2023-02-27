# Function to generate Fibonacci Triangle
def fibonacci_triangle(n):
    # Initializing first two terms of Fibonacci series
    a, b = 0, 1
    # Generating Fibonacci Triangle
    for i in range(n):
        # Printing ith row of Fibonacci Triangle
        for j in range(i+1):
            # Printing the ith Fibonacci number
            print(b, end=" ")
            # Updating the Fibonacci numbers
            a, b = b, a + b
        print()

# Taking input from user
n = int(input("Enter the number of rows for Fibonacci Triangle: "))

# Printing the Fibonacci Triangle
print("The Fibonacci Triangle of", n, "rows is:")
fibonacci_triangle(n)