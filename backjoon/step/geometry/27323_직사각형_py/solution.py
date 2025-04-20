import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  height = int(input())
  width = int(input())

  print(height * width)


if __name__ == '__main__':
  solve()
