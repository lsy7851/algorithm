import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  sides = list(map(int, input().split()))
  sides.sort()

  if sides[0] + sides[1] <= sides[2]:
    sides[2] = sides[0] + sides[1] - 1

  print(sum(sides))


if __name__ == '__main__':
  solve()
