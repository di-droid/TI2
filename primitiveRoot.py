import math
import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)


def primitive_roots(modulo):
    prime_set = {num for num in range(1, modulo) if math.gcd(num, modulo) == 1}
    temp = [i for i in range(1, modulo) if prime_set == {mod_exp(i, powers, modulo) for powers in range(1, modulo)}]
    return tuple(temp)


def find_primitive_root(modulo):
    mn = 2
    mx = (modulo - 1) // mn

    while 1:
        root = random.randint(2, modulo - 1)
        if not (mod_exp(root, (modulo - 1) // mn, modulo) == 1):
            if not mod_exp(root, (modulo - 1) // mx, modulo) == 1:
                return root
