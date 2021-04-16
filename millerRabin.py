import random
from algorithms import fast_pow


def is_prime_test(number, num_of_tests=5):
    s = 0
    d = number - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert(fast_pow(2, s) * d == number - 1)

    def trial_composite(a):
        if pow(a, d, number) == 1:
            return False
        for ind in range(s):
            if pow(a, fast_pow(2, ind) * d, number) == number - 1:
                return False
        return True

    for i in range(num_of_tests):
        num = random.randrange(2, number)
        if trial_composite(num):
            return False

    return True
