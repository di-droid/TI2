import math


def fast_pow(number, power):
    if power == 0:
        return 1
    elif power == -1:
        return 1. / number

    p = fast_pow(number, power // 2)
    p *= p

    if power % 2:
        p *= number

    return p


def rus_multiplication(first_num, second_num):
    temp = 0
    while second_num > 0:
        if second_num % 2 == 1:
            temp = temp + first_num

        first_num = first_num << 1
        second_num = second_num >> 1
    return temp


def is_prime(number):
    i = 2
    while rus_multiplication(i, i) <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def co_prime(p, k):
    return math.gcd(p, k) == 1


def eratosthenes_sieve(n):
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

    return tuple(lst)

