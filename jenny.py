# Time Limit Exceeded

import sys


def is_prime(n: int):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_jenny(n: int):
    if is_prime(n) is False:
        return False

    # check if next odd number is prime
    if n % 2 == 0:
        if is_prime(n+1) is False:
            return False
    else:
        if is_prime(n+2) is False:
            return False

    n_str = str(n)
    for i in range(1, len(n_str)):
        for j in range(i):
            if n_str[i] == n_str[j]:
                return False  # repeated digits

    return True


for line in sys.stdin:
    line = line.rstrip('\n')

    try:
        d = int(line[0])  # this use of indices doesn't even consider d being two digits
        i = int(line[2])  # IndexError on first line
        result_exists = False
        count = 0
        for n in range(10 ** (d - 1), 10 ** d):
            if is_jenny(n):
                count += 1
                if count == i:
                    print(n)
                    result_exists = True
                    break
        if result_exists is False:
            print("Brice doesn't stand a chance!")

    except IndexError:
        pass
