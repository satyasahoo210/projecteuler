def isPrime(n):
  for d in range(2, int(n ** .5 + 1)):
    if n % d == 0:
      return False
  return True

def solution(num: int) -> int:
  for d in range(int(num ** .5 + 1), 2, -1):
    if num % d == 0 and isPrime(d):
      return d

if __name__ == '__main__':
  print(solution(600851475143))
