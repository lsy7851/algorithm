import sys

input = lambda: sys.stdin.readline().rstrip()


def is_prime(number):
  if number == 1:
    return False

  for i in range(2, int(number ** 0.5 + 1)):
    if number % i == 0:
      return False

  return True


def solve():
  input()  # useless input
  numbers = map(int, input().split())
  primes = list(filter(lambda x: is_prime(x), numbers))
  print(len(primes))


if __name__ == '__main__':
  solve()
