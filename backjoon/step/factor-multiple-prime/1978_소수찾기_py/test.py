from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1:
  # N = 1, 입력 정수: 1 → 소수가 아님 → 소수의 개수 0
  (
    "1\n1\n",
    "0\n"
  ),
  # 테스트 케이스 2:
  # N = 1, 입력 정수: 2 → 2는 소수 → 소수의 개수 1
  (
    "1\n2\n",
    "1\n"
  ),
  # 테스트 케이스 3:
  # N = 4, 입력: 1, 2, 3, 4 → 소수: 2, 3 → 개수 2
  (
    "4\n1 2 3 4\n",
    "2\n"
  ),
  # 테스트 케이스 4:
  # N = 5, 입력: 3, 4, 5, 6, 7 → 소수: 3, 5, 7 → 개수 3
  (
    "5\n3 4 5 6 7\n",
    "3\n"
  ),
  # 테스트 케이스 5:
  # N = 7, 입력: 67, 98, 59, 2, 3, 8, 5 → 소수: 67, 59, 2, 3, 5 → 개수 5
  (
    "7\n67 98 59 2 3 8 5\n",
    "5\n"
  ),
  # 테스트 케이스 6:
  # N = 8, 입력: 12, 77, 38, 41, 53, 92, 65, 89 → 소수: 41, 53, 89 → 개수 3
  (
    "8\n12 77 38 41 53 92 65 89\n",
    "3\n"
  ),
  # 테스트 케이스 7:
  # N = 10, 입력: 97, 2, 3, 4, 5, 6, 7, 8, 9, 10 → 소수: 97, 2, 3, 5, 7 → 개수 5
  (
    "10\n97 2 3 4 5 6 7 8 9 10\n",
    "5\n"
  ),
  # 테스트 케이스 8:
  # N = 3, 입력: 11, 13, 17 → 모두 소수 → 개수 3
  (
    "3\n11 13 17\n",
    "3\n"
  ),
  # 테스트 케이스 9:
  # N = 3, 입력: 14, 15, 16 → 소수 없음 → 개수 0
  (
    "3\n14 15 16\n",
    "0\n"
  ),
  # 테스트 케이스 10:
  # N = 6, 입력: 1, 2, 3, 4, 5, 6 → 소수: 2, 3, 5 → 개수 3
  (
    "6\n1 2 3 4 5 6\n",
    "3\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
