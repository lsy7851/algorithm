import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()


def solve():
  city_count = int(input())
  road_lengths = list(map(int, input().split()))
  oil_costs = list(map(int, input().split()))
  load_length_prefix_sum = [0] + list(accumulate(road_lengths))

  total_cost = 0
  current_city = 0

  while current_city < city_count - 1:
    for next_city in range(current_city + 1, city_count):

      is_last_city = next_city == city_count - 1
      find_low_cost_city = oil_costs[current_city] > oil_costs[next_city]

      if is_last_city or find_low_cost_city:
        distance = load_length_prefix_sum[next_city] - load_length_prefix_sum[current_city]
        total_cost += oil_costs[current_city] * distance
        current_city = next_city
        break

  print(total_cost)


if __name__ == '__main__':
  solve()
