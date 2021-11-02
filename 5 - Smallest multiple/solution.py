# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
# def solution(n):
#   def isDivisible(num):
#     for i in range(2, n):
#       if num % i != 0:
#         return False
#     return True

#   _num = n
#   while True:
#     if isDivisible(_num):
#       print(_num, isDivisible(_num))
#       return _num
#     else:
#       _num += 1

# if __name__ == '__main__':
#   print(solution(20))

from itertools import count, takewhile


def primes(n):
    "Generate prime numbers up to n"
    seen = list()
    for i in range(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i


def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x: x <= n,
                               (prime ** c for c in count(1))))
        # we could just take last instead of max()
        result *= bprime
    return result


print(smallest(20))
