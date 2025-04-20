import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  x, y = map(int, input().split())
  x2, y2 = map(int, input().split())
  x3, y3 = map(int, input().split())

  x_list = [x, x2, x3]
  y_list = [y, y2, y3]
  result_x = 0
  result_y = 0

  for x_val in x_list:
    if x_list.count(x_val) == 1:
      result_x = x_val
      break

  for y_val in y_list:
    if y_list.count(y_val) == 1:
      result_y = y_val
      break

  print(result_x, result_y)


if __name__ == '__main__':
  solve()
