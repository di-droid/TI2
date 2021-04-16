import random
from algorithms import fast_pow, eratosthenes_sieve, co_prime
from millerRabin import is_prime_test
from primitiveRoot import find_primitive_root


class PublicKey:
    def __init__(self, p, g, y):
        self.p = p
        self.g = g
        self.y = y


class Couple:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def generate_p(first_bit, last_bit):
    min_p = fast_pow(2, first_bit) / 2
    max_p = fast_pow(2, last_bit) - 1

    sieve = eratosthenes_sieve(5000)

    while 1:
        p = random.randrange(min_p, max_p)
        if p % 2 == 0:
            continue

        for i in sieve:
            if p % i == 0:
                continue

        if is_prime_test(p, 8):
            return p


def generate_g(p):
    return find_primitive_root(p)


def generate_x(p):
    return random.randrange(2, p - 1)


def calculate_y(p, g, x):
    return pow(g, x, p)


def generate_keys(first_bit=128, second_bit=256):
    p = generate_p(first_bit, second_bit)
    g = generate_g(p)
    x = generate_x(p)
    y = calculate_y(p, g, x)

    public_key = PublicKey(p, g, y)
    return public_key, x


def generate_k(p):
    while 1:
        k = random.randrange(1, p - 1)
        if co_prime(k, p - 1):
            return k


def encryption(m, public_key):
    message = []
    for sym in m:
        k = generate_k(public_key.p)

        a = pow(public_key.g, k, public_key.p)
        b = (sym * pow(public_key.y, k, public_key.p)) % public_key.p

        message.append(Couple(a, b))
    return message


def decryption(m, public_key, private_key):
    message = []
    for couple in m:
        temp = (couple.b * pow(couple.a, -private_key, public_key.p)) % public_key.p
        message.append(temp)
    return message
