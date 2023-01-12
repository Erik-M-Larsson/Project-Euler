import math


def check_if_prime(n: int) -> bool:
    """Check if n is a prime number"""
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True


def find_largest_prime_factor(n: int) -> int:
    """Finds and return the largest prime factor in n. If there is no prime factors (i.e. prime number) return None"""

    if check_if_prime(n):
        return

    for i in range(2, int(math.sqrt(n) + 1)):

        if check_if_prime(i):

            if n % i == 0:
                candidate_factor = n // i
                # print("candidate_factor", candidate_factor)

                if check_if_prime(candidate_factor):
                    return candidate_factor

                else:

                    return find_largest_prime_factor(candidate_factor)


def prime_factors(n: int, multiples: bool = True) -> list[int]:
    """Finds alla prime factors of n. Including multiples if multiples == True. Returns all prime factors as a list"""

    list_of_prime_factors = []

    for i in range(2, n + 1):

        while n % i == 0:
            list_of_prime_factors.append(i)
            n /= i
            if n == 1:
                return list_of_prime_factors

    return list_of_prime_factors if multiples else list(set(list_of_prime_factors))
