import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  angle = int(input())
  angle2 = int(input())
  angle3 = int(input())

  if sum([angle, angle2, angle3]) != 180:
    print('Error')
    return

  if angle == 60 and angle2 == 60:
    print('Equilateral')
    return

  if angle == angle2 or angle2 == angle3 or angle == angle3:
    print('Isosceles')
    return

  print('Scalene')


if __name__ == '__main__':
  solve()
