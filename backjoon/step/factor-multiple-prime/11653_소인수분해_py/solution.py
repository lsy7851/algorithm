import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  number = int(input())
  prime = 2

  while prime * prime <= number:
    while number % prime == 0:
      number = number // prime
      print(prime)
    prime += 1
  if 1 < number:
    print(number)


if __name__ == '__main__':
  solve()
