def print_primes(N):
    # Create a boolean array "is_prime[0..N]" and initialize
    # all entries as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (N+1)
    p = 2
    while p**2 <= N:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p greater than or equal to p^2
            # numbers which are multiple of p and are less than p^2
            # are already been marked.
            for i in range(p**2, N+1, p):
                is_prime[i] = False
        p += 1
    # Print all prime numbers
    for p in range(2, N+1):
        if is_prime[p]:
            print(p)

# Example usage
print_primes(10)  # Output: 2 3 5 7
print_primes(20)  # Output: 2 3 5 7 11 13 17 19
print_primes(30)  # Output: 2 3 5 7 11 13 17 19 23 29