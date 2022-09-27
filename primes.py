"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError

    res = []

    i = 2

    while len(res) < number_of_primes:
        prime = True
        for j in range(2, i - 1):
            if i // j == i / j:
                prime = False
        if prime:
            res.append(i)
        i += 1
        
    return res
