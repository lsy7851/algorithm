import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  input()
  number_list = input()

  sum = 0
  for num_str in number_list:
    sum += int(num_str)

  print(sum)


if __name__ == '__main__':
  solve()
