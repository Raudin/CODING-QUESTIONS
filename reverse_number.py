def reverse_number(num):
    # Convert the number to a string
    num_str = str(num)
    # Reverse the string
    reversed_str = num_str[::-1]
    # Convert the reversed string back to a number
    reversed_num = int(reversed_str)
    # Return the reversed number
    return reversed_num

# Example usage
print(reverse_number(12345))  # Output: 54321
print(reverse_number(987654321))  # Output: 123456789
print(reverse_number(100))  # Output: 1