import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  bead_count = int(input())
  coordinate_x = []
  coordinate_y = []

  for _ in range(bead_count):
    x, y = (map(int, input().split()))
    coordinate_x.append(x)
    coordinate_y.append(y)

  min_x = min(coordinate_x)
  min_y = min(coordinate_y)
  max_x = max(coordinate_x)
  max_y = max(coordinate_y)

  print((max_x - min_x) * (max_y - min_y))


if __name__ == '__main__':
  solve()
