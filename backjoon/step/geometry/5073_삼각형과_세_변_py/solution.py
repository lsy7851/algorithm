import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  while True:
    sides = list(map(int, input().split()))

    if sum(sides) == 0:
      break

    sides.sort()

    if sides[0] + sides[1] <= sides[2]:
      print('Invalid')
      continue

    if sides.count(sides[0]) == 3:
      print('Equilateral')
      continue

    if sides.count(sides[0]) == 2 or sides.count(sides[1]) == 2:
      print('Isosceles')
      continue

    print('Scalene')


if __name__ == '__main__':
  solve()
