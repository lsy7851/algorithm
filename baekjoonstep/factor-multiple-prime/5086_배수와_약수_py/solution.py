import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  while True:
    number, target = map(int, input().split())
    if number == 0 and target == 0:
      break

    if target % number == 0:
      print("factor")
      continue
    if number % target == 0:
      print("multiple")
      continue
    print("neither")


if __name__ == '__main__':
  solve()
