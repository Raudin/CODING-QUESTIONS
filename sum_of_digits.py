def sum_of_digits(num):
    sum = 0
    while num > 0:
        # Get the last digit of the number
        digit = num % 10
        # Add the digit to the sum
        sum += digit
        # Remove the last digit from the number
        num //= 10
    return sum

# Example usage
print(sum_of_digits(123))  # Output: 6 (1 + 2 + 3)
print(sum_of_digits(4567))  # Output: 22 (4 + 5 + 6 + 7)