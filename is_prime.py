import math

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

# Example usage
num = 17
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")