import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  people_count = int(input())

  wait_times = list(map(int, input().split()))
  wait_times.sort(key=lambda x: x)

  prefix_sum_wait_times = [0] * people_count
  prefix_sum_wait_times[0] = wait_times[0]

  for i in range(1, people_count):
    prefix_sum_wait_times[i] = prefix_sum_wait_times[i - 1] + wait_times[i]

  print(sum(prefix_sum_wait_times))


if __name__ == '__main__':
  solve()
