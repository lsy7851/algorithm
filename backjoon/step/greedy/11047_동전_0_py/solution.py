import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  coin_kind, goal_value = map(int, input().split())

  coins = [int(input()) for _ in range(coin_kind)][::-1]

  coin_count = 0

  for coin_value in coins:
    coin_count += goal_value // coin_value
    goal_value = goal_value % coin_value

  print(coin_count)


if __name__ == '__main__':
  solve()
