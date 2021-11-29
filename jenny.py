# Time Limit Exceeded

import sys
import time


def is_prime(n: int):
    if n == 1:
        return False
    elif n % 2 == 0 and n != 2:
        return False
    for i in range(2, (n+1)//2):
        if n % i == 0:
            return False
    return True


def is_jenny(n: int):
    if is_prime(n) is False:
        return False

    if is_prime(n+2) is False:
        if n != 2:
            return False

    n_str = str(n)
    for i in range(len(n_str)):
        if n_str.count(n_str[i]) > 1:
            return False

    return True


for line in sys.stdin:
    start_time = time.time()
    line = line.rstrip('\n').split()

    try:
        d = int(line[0])
        i = int(line[1])  # IndexError on first line
        result_exists = False
        count = 0
        n = 10 ** (d - 1)  # start
        while n <= 10 ** d:
            if is_jenny(n):
                count += 1
                if count == i:
                    print(n)
                    result_exists = True
                    print("Runtime (s): " + str(time.time() - start_time))
                    break
            n += 1
        if result_exists is False:
            print("Brice doesn't stand a chance!")
            print("Runtime (s): " + str(time.time() - start_time))

    except IndexError:
        pass
