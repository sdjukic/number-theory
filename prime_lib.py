# Library for dealing with prime numbers
from math import sqrt

def is_prime(number):
    if number % 2 == 0 or number % 3 == 0: return False
    for divisor in range(5, int(sqrt(number)+1), 2):
        if number % divisor == 0: return False

    return True

# intuitive implementation of sieve
def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i*i, limit, i): #Mark factors non-prime
                a[n] = False


# this is from active state
def postponed_sieve():
    yield 2; yield 3; yield 5; yield 7;
    sieve = {}
    ps = (p for p in postponed_sieve())    # a separate Primes supply
    p = next(ps) and next(ps)              # (3) a Prime to add to dict
    q = p*p                                # (9) when its square
    c = 9                                  # is the next candidate
    
    while True:
        if c not in sieve:                 # not a multiple of any prime seen so far
            if c < q:                      # a prime
                yield c; c += 2;
                continue
            else:   # (c==q)               # the next prime's square:
                s = 2*p                    # (9+6, 6 : 15, 21, 27, 33,...)
                p = next(ps)               # (5)
                q = p*p                    # (25)
        else:                              # 'c' is a composite
            s = sieve.pop(c)               # step of increment
        c2 = c + s                         # next multiple, same step
        while c2 in sieve:                 # no multiple key in sieve (dict):
            c2 += s                        #  (increments by the given step)
        sieve[c2] = s                   
        c += 2                             # next odd candidate

  
def gcd(number_one, number_two):
    """Function implements Euclid's algorithm to find gcd of its arguments."""
    bigger = max(number_one, number_two)
    smaller = min(number_one, number_two)

    remainder = 1
    while remainder:
        remainder = bigger - smaller * (bigger // smaller)
        bigger, smaller = smaller, remainder

    return bigger
    
def prime_factors(number):
    """Function that returns list of prime factors of a number."""
    prime_generator = postponed_sieve()
    result = []
    upper_limit = int(sqrt(number) + 1)
    
    while True:
        prime = prime_generator.next()
        if prime > upper_limit:
            break
        else:
            if number % prime == 0:
                result.append(prime)
                while number % prime == 0:
                    number /= prime
                    
    if number != 1:
        if is_prime(number):
            result.append(number)
            
    return result
    
    
def euler_phi(number):
    """Function that calculates Euler's phi of a number."""
    result = number
    factors = prime_factors(number)
    
    for factor in factors:
      result *= (1 - (1.0 / factor))

    return int(result)
        
