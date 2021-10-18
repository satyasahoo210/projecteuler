# Find the sum of all the multiples of 3 or 5 below 1000.
def mutiples(below=1000):
  return sum(
    [
      i
      for i in range(below)
      if i % 3 == 0 or i % 5 == 0
    ]
  )


if __name__ == '__main__':
  sm = mutiples()
  print(sm)
