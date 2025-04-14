import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  city_count = int(input())
  road_length = list(map(int, input().split()))
  oil_cost = list(map(int, input().split()))

  total_cost = 0
  most_chip_cost = oil_cost[0]

  for now_city in range(1, city_count):
    total_cost += most_chip_cost * road_length[now_city - 1]
    if oil_cost[now_city] < most_chip_cost:
      most_chip_cost = oil_cost[now_city]

  print(total_cost)


if __name__ == '__main__':
  solve()
