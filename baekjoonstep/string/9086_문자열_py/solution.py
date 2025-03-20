import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  case_count = int(input())

  for i in range(case_count):
    case = input()
    print(case[0] + case[-1])


if __name__ == '__main__':
  solve()
