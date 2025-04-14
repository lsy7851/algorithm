import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  number, target_rank = map(int, input().split())
  factors = list(filter(lambda x: x > 0, [i if number % i == 0 else -1 for i in range(1, number // 2 + 1)] + [number]))

  if len(factors) < target_rank:
    print(0)
  else:
    print(factors[target_rank - 1])


if __name__ == '__main__':
  solve()
