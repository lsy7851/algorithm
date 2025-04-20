from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1) 3, 4, 5 → 3+4 > 5 이므로 그대로 합 = 12
  (
    "3 4 5\n",
    "12\n"
  ),
  # 2) 1, 2, 3 → 1+2 = 3 ≤ 3 이므로 2*(1+2)-1 = 5
  (
    "1 2 3\n",
    "5\n"
  ),
  # 3) 100, 1, 1 → 1+1 = 2 ≤ 100 이므로 2*2-1 = 3
  (
    "100 1 1\n",
    "3\n"
  ),
  # 4) 10, 10, 10 → 10+10 > 10 이므로 합 = 30
  (
    "10 10 10\n",
    "30\n"
  ),
  # 5) 5, 5, 10 → 5+5 = 10 ≤ 10 이므로 2*10-1 = 19
  (
    "5 5 10\n",
    "19\n"
  ),
  # 6) 6, 7, 2 → 정렬 후 (2,6,7), 2+6 = 8 > 7 이므로 합 = 15
  (
    "6 7 2\n",
    "15\n"
  ),
  # 7) 1, 1, 2 → 1+1 = 2 ≤ 2 이므로 2*2-1 = 3
  (
    "1 1 2\n",
    "3\n"
  ),
  # 8) 8, 12, 3 → 정렬 후 (3,8,12), 3+8 = 11 ≤ 12 이므로 2*11-1 = 21
  (
    "8 12 3\n",
    "21\n"
  ),
  # 9) 9, 15, 27 → 정렬 후 (9,15,27), 9+15 = 24 ≤ 27 이므로 2*24-1 = 47
  (
    "9 15 27\n",
    "47\n"
  ),
  # 10) 큰 값 테스트: 1e9,1e9,1e9 → 각 합 3e9
  (
    "1000000000 1000000000 1000000000\n",
    "3000000000\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
