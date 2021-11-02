# Find the largest palindrome made from the product of two 3-digit numbers.
def isPallindrome(n):
  s = str(n)
  return s == s[::-1]

def solution(ndigits):
  _min = 10 ** (ndigits-1)
  _max = 10 ** ndigits - 1
  result = 0,0
  p = 0

  for i in range(_max, _min -1, -1):
    for j in range(_max, i-1, -1):
      if p < i*j and isPallindrome(i*j):
        result = i,j
        p = i*j

  return result

if __name__ == '__main__':
  a,b = solution(3)
  m = a*b
  print('{} * {} = {}'.format(a,b,m))
