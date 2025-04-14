import sys

input = lambda: sys.stdin.readline().rstrip()


def calc_proper_divisor(number):
  proper_divisor = [1] # 진약수 리스트
  for i in range(2, int(number ** 0.5 + 1)):
    if number % i == 0:
      proper_divisor.append(i)
      proper_divisor.append(number // i)
  proper_divisor.sort()
  return proper_divisor


def solve():
  while True:
    number = int(input())
    if number == -1:
      break

    proper_divisor = calc_proper_divisor(number)
    if sum(proper_divisor) == number:
      print('{} = {}'.format(number, ' + '.join(map(str, proper_divisor))))
    else:
      print('{} is NOT perfect.'.format(number))


if __name__ == '__main__':
  solve()
