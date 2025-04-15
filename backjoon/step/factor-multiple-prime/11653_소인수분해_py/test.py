from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1:
  # N = 1 → 출력 없음
  (
    "1\n",
    ""
  ),
  # 테스트 케이스 2:
  # N = 2 → 2는 소수 → 출력: "2"
  (
    "2\n",
    "2\n"
  ),
  # 테스트 케이스 3:
  # N = 3 → 3는 소수 → 출력: "3"
  (
    "3\n",
    "3\n"
  ),
  # 테스트 케이스 4:
  # N = 4 → 4 = 2 * 2 → 출력: "2", "2"
  (
    "4\n",
    "2\n2\n"
  ),
  # 테스트 케이스 5:
  # N = 6 → 6 = 2 * 3 → 출력: "2", "3"
  (
    "6\n",
    "2\n3\n"
  ),
  # 테스트 케이스 6:
  # N = 16 → 16 = 2^4 → 출력: "2" 네 번
  (
    "16\n",
    "2\n2\n2\n2\n"
  ),
  # 테스트 케이스 7:
  # N = 100 → 100 = 2^2 * 5^2 → 출력: "2", "2", "5", "5"
  (
    "100\n",
    "2\n2\n5\n5\n"
  ),
  # 테스트 케이스 8:
  # N = 123456
  # 123456 ÷2=61728, ÷2=30864, ÷2=15432, ÷2=7716, ÷2=3858, ÷2=1929,
  # 1929 ÷3=643, 643는 소수.
  # → 123456 = 2^6 * 3 * 643 → 출력: 2를 6번, 그 다음 3, 그 다음 643.
  (
    "123456\n",
    "2\n2\n2\n2\n2\n2\n3\n643\n"
  ),
  # 테스트 케이스 9:
  # N = 10000000
  # 10000000 = 10^7 = (2*5)^7 = 2^7 * 5^7
  # → 출력: 2를 7번, 그 다음 5를 7번.
  (
    "10000000\n",
    "2\n2\n2\n2\n2\n2\n2\n5\n5\n5\n5\n5\n5\n5\n"
  ),
  # 테스트 케이스 10:
  # N = 462
  # 462 = 2 * 3 * 7 * 11
  # → 출력: "2", "3", "7", "11"
  (
    "462\n",
    "2\n3\n7\n11\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
