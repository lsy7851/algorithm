from not_greedy_solution import solve as not_grid
from solution import solve
from util.test_runner import run_fun_solution


def generate_test_cases():
  test_cases = []

  # Test Case 1: n = 5000, 모든 도시간 거리가 100, 모든 기름 가격이 100
  n = 5000
  distances = [100] * (n - 1)
  prices = [100] * n
  total_distance = sum(distances)  # 4999 * 100 = 499900
  cost = 100 * total_distance  # 100 * 499900 = 49990000
  input_str = f"{n}\n" + " ".join(map(str, distances)) + "\n" + " ".join(map(str, prices))
  output_str = f"{cost}\n"
  test_cases.append((input_str, output_str))

  # Test Case 2: n = 6000, 모든 도시간 거리가 10000, 모든 기름 가격이 10000
  n = 6000
  distances = [10000] * (n - 1)
  prices = [10000] * n
  total_distance = sum(distances)  # 5999 * 10000 = 59990000
  cost = 10000 * total_distance  # 10000 * 59990000 = 599900000000
  input_str = f"{n}\n" + " ".join(map(str, distances)) + "\n" + " ".join(map(str, prices))
  output_str = f"{cost}\n"
  test_cases.append((input_str, output_str))

  # Test Case 3:
  # n = 7000,
  # 도시간 거리는 패턴 [100, 500, 1000, 2000, 3000]를 반복하여 총 6999개 생성
  # 기름 가격은 100부터 1씩 증가하는 수열 (7000개)
  n = 7000
  pattern = [100, 500, 1000, 2000, 3000]
  distances = [pattern[i % len(pattern)] for i in range(n - 1)]
  prices = [100 + i for i in range(n)]
  total_distance = sum(distances)
  # 기름 가격이 계속 증가하므로, 첫 도시의 가격인 100이 항상 최소 가격이 됨
  cost = 100 * total_distance
  input_str = f"{n}\n" + " ".join(map(str, distances)) + "\n" + " ".join(map(str, prices))
  output_str = f"{cost}\n"
  test_cases.append((input_str, output_str))

  # Test Case 4:
  # n = 8000,
  # 모든 도시간 거리가 5000,
  # 기름 가격은 10000부터 1씩 감소하는 수열: [10000, 9999, ..., 2001]
  n = 8000
  distances = [5000] * (n - 1)
  prices = [10000 - i for i in range(n)]
  # 기름 가격이 내림차순이므로, i번째 구간의 최소 가격은 prices[i]가 됨 (i=0부터 n-2까지)
  total_price = sum(prices[:-1])
  cost = 5000 * total_price
  input_str = f"{n}\n" + " ".join(map(str, distances)) + "\n" + " ".join(map(str, prices))
  output_str = f"{cost}\n"
  test_cases.append((input_str, output_str))

  # Test Case 5:
  # n = 10000,
  # 도시간 거리는 패턴 [100, 10000, 5000]를 반복 (총 9999개, 9999가 3의 배수이므로 정확히 반복됨)
  # 기름 가격은 홀수 도시는 100, 짝수 도시는 10000 (즉, 첫 도시는 100, 두 번째는 10000, 세 번째는 100, …)
  n = 10000
  pattern = [100, 10000, 5000]
  distances = [pattern[i % len(pattern)] for i in range(n - 1)]
  prices = [100 if i % 2 == 0 else 10000 for i in range(n)]
  total_distance = sum(distances)
  # 첫 도시의 기름 가격이 100이므로 전체 최소 가격은 100로 계산됨
  cost = 100 * total_distance
  input_str = f"{n}\n" + " ".join(map(str, distances)) + "\n" + " ".join(map(str, prices))
  output_str = f"{cost}\n"
  test_cases.append((input_str, output_str))

  return test_cases

test_cases = [
  ("4\n2 3 1\n5 2 4 1", "18\n"),
  ("4\n3 3 4\n1 1 1 1", "10\n"),
  ("2\n10\n5 3", "50\n"),
  ("2\n1\n1000 1", "1000\n"),
  ("5\n2 3 1 4\n3 4 5 6 7", "30\n"),
  ("5\n2 3 1 4\n7 6 5 4 3", "53\n"),
  ("6\n5 4 3 2 1\n5 2 4 2 2 1", "45\n"),
  ("6\n3 2 5 1 1\n4 3 2 4 1 5", "31\n"),
  ("7\n1 1 1 1 1 1\n5 5 5 5 5 5 5", "30\n"),
  ("7\n2 2 2 2 2 2\n3 1 2 1 3 1 2", "16\n"),
  ("8\n3 1 2 3 1 2 3\n5 4 3 2 1 2 3 4", "37\n"),
  ("8\n5 5 5 5 5 5 5\n8 7 6 5 4 3 2 1", "175\n"),
  ("10\n1 2 3 4 5 6 7 8 9\n9 8 7 6 5 4 3 2 1 10", "165\n"),
  ("10\n10 10 10 10 10 10 10 10 10\n1 1 1 1 1 1 1 1 1 1", "90\n"),
  ("6\n100 1 50 1 100\n5 3 2 4 1 2", "705\n"),
  ("3\n1000 1000\n1 100 1", "2000\n"),
  ("3\n500 500\n10 10 1", "10000\n"),
  ("9\n1 3 5 7 9 11 13 15\n8 6 7 4 5 2 3 1 9", "183\n"),
  ("9\n10 9 8 7 6 5 4 3\n9 9 9 9 9 9 9 9 9", "468\n"),
  ("10\n2 2 2 2 2 2 2 2 2\n3 2 1 1 1 1 1 1 1 1", "24\n"),
  ("5\n5 3 7 3\n4 2 8 1 3", "43\n"),
  ("6\n3 5 2 6 7\n5 5 4 4 2 10", "86\n"),
  ("7\n10 10 10 10 10 10\n5 4 3 2 1 2 3", "160\n"),
  ("8\n1 1 1 1 1 1 1\n10 10 10 10 10 10 10 10", "70\n"),
  ("9\n5 6 7 8 9 10 11 12\n8 7 6 5 4 3 2 1 9", "264\n"),
  ("10\n10 10 5 5 10 5 5 10 10\n3 3 3 2 2 1 1 1 1 1", "135\n"),
  ("12\n1 2 1 2 1 2 1 2 1 2 1\n9 8 7 6 5 4 3 2 1 2 3 4", "68\n"),
  ("11\n100 50 50 100 50 50 100 50 50 100\n10 9 8 7 6 5 4 3 2 1 1", "3850\n"),
  ("15\n3 14 15 92 65 35 89 79 32 38 46 26 43 38\n5 4 3 9 2 6 5 5 3 5 8 9 7 3 2", "1374\n"),
  (
    """20
    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
    10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 11
    """,
    "11166\n"
  ),
  ("5\n7 3 9 1\n2 10 1 5 2", "30\n"),
  ("6\n2 2 2 2 2\n5 4 3 2 3 1", "32\n"),
  ("7\n20 20 20 20 20 20\n7 6 5 4 3 2 1", "540\n"),
  ("8\n12 12 12 12 12 12 12\n3 5 1 7 2 8 6 4", "132\n"),
  ("9\n3 3 3 3 3 3 3 3\n9 1 8 1 8 1 8 1 8", "48\n"),
  ("10\n5 5 5 5 5 5 5 5 5\n1 2 3 4 5 6 7 8 9 10", "45\n"),
  ("5\n100 200 300 400\n100 50 25 75 10", "37500\n"),
  ("6\n7 11 13 17 19\n11 13 17 19 23 29", "737\n"),
  ("7\n50 50 50 50 50 50\n8 7 6 7 6 5 4", "1900\n"),
  ("10\n9 9 9 9 9 9 9 9 9\n5 4 3 4 3 2 2 1 1 1", "216\n"),
] + generate_test_cases()


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"


def test_not_grid():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, not_grid)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
