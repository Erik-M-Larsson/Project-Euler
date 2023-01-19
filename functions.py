import math
import numpy as np
from itertools import count
from collections.abc import Iterable
from typing import Any


def permutations_repetition(iterable: Iterable[Any], n: int, /) -> list[list[Any]]:
    """All permutations with repetition of n elements from iterable"""
    λ = len(iterable)
    return [
        [iterable[int((row % λ ** col) / λ ** (col - 1))] for col in range(n, 0, -1)]
        for row in range(λ ** n)
    ]


def prime_mask(N: int) -> np.ndarray[bool]:
    """Gives a bolean ndarray of for all integers up to N. True if prime number else False"""
    primes = np.ones(N + 1, bool)
    primes[0:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if primes[i]:
            primes[2 * i :: i] = False
    return primes


def check_if_prime(n: int) -> bool:
    """Check if n is a prime number"""
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True


def prime_generator(start: int = 2) -> int:
    """Generates prime numbers in ascending order. If start value is given the first prime number >= start"""

    if check_if_prime(start):
        yield start

    for n in count(start + 1, 2):

        if check_if_prime(n):
            yield n


def find_largest_prime_factor(n: int) -> int:
    """Finds and return the largest prime factor in n. If there is no prime factors (i.e. prime number) return None"""

    if check_if_prime(n):
        return

    for i in range(2, int(math.sqrt(n) + 1)):

        if check_if_prime(i):

            if n % i == 0:
                candidate_factor = n // i

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
                return (
                    list_of_prime_factors
                    if multiples
                    else list(set(list_of_prime_factors))
                )

    return list_of_prime_factors if multiples else list(set(list_of_prime_factors))
