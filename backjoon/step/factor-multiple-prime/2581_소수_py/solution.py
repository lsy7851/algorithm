import sys

input = lambda: sys.stdin.readline().rstrip()


def sieve_of_eratosthenes(max):
  is_primes = [True] * (max + 1)
  is_primes[0] = False
  is_primes[1] = False
  for i in range(2, int(max ** 0.5 + 1)):
    if is_primes[i] is True:
      for j in range(i * 2, max + 1, i):
        is_primes[j] = False
  return is_primes


def solve():
  start = int(input())
  end = int(input())
  is_primes = sieve_of_eratosthenes(end)
  primes = list(filter(lambda x: is_primes[x], range(start, end + 1)))
  if len(primes) == 0:
    print(-1)
    return

  print(sum(primes))
  print(primes[0])


if __name__ == '__main__':
  solve()
