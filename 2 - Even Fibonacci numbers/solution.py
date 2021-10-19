# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def solution(limit=4000000):
  a,b = 0,1
  sm = 0
  while b < limit:
    a, b = b, a+b
    if not b & 1:
      sm += b

  return sm

if __name__ == '__main__':
  sm = solution()
  print(sm)
