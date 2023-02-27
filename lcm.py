def lcm(num1, num2):
    # Find the maximum of the two numbers
    max_num = max(num1, num2)

    # Start with the maximum number and check each multiple until a common multiple is found
    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break
        max_num += 1

    return lcm

# Example usage
print(lcm(12, 18))  # Output: 36
print(lcm(5, 7))  # Output: 35