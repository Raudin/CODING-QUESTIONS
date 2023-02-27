# Function to find sum of A.P series
def sum_of_ap(a, d, n):
    # Using formula for sum of A.P series
    sum = (n/2) * (2*a + (n-1)*d)
    return int(sum)

# Taking input from user
a = int(input("Enter the first term of A.P: "))
d = int(input("Enter the common difference of A.P: "))
n = int(input("Enter the number of terms in A.P: "))

# Printing the sum of A.P series
print("The sum of", n, "terms of A.P series is", sum_of_ap(a, d, n))