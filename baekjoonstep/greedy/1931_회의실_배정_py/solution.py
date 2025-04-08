import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  meeting_count = int(input())

  meetings = sorted(
    [tuple(map(int, input().split())) for _ in range(meeting_count)],
    key=lambda x: (x[1], x[0])
  )

  end_time = 0
  max_meet_count = 0

  for start, end in meetings:
    if end_time <= start:
      max_meet_count += 1
      end_time = end

  print(max_meet_count)


if __name__ == '__main__':
  solve()
