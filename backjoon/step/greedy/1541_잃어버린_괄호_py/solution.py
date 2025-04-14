import sys

input = lambda: sys.stdin.readline().rstrip()


def to_operand(subexpression):
  if '+' in subexpression:
    return sum(map(int, subexpression.split('+')))

  return int(subexpression)


def solve():
  expression = input()
  subexpressions = expression.split('-')
  operands = [to_operand(subexpression) for subexpression in subexpressions]
  print(operands[0] - sum(operands[1:]))


if __name__ == '__main__':
  solve()
