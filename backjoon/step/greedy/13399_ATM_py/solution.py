import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  input() # useless input

  wait_times = list(map(int, input().split()))
  wait_times.sort(key=lambda x: x, reverse=True)

  total_wait_time = [time * (index + 1) for index, time in enumerate(wait_times)]
  print(sum(total_wait_time))


if __name__ == '__main__':
  solve()
