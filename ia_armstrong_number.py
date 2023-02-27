def is_armstrong_number(num):
    # Convert number to string to count its digits
    num_str = str(num)
    n = len(num_str)
    # Calculate the sum of each digit raised to the power of n
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
    # Check if the sum is equal to the original number
    if sum == num:
        return True
    else:
        return False
