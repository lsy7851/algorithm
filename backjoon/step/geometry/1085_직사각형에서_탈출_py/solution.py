import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  x, y, w, h = map(int, input().split())

  print(min(x, y, w - x, h - y))


if __name__ == '__main__':
  solve()
