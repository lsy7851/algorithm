from solution import solve
from util.test_runner import run_fun_solution

test_cases = [

  # 테스트 케이스 1:
  # 단일 테스트 케이스 → (20, 5): 20 > 5, 20 % 5 == 0 → "multiple"
  (
    "20 5\n0 0\n",
    "multiple\n"
  ),
  # 테스트 케이스 2:
  # (10, 5): 10 > 5, 10 % 5 == 0 → "multiple"
  (
    "10 5\n0 0\n",
    "multiple\n"
  ),
  # 테스트 케이스 3:
  # (5, 10): 5 < 10, 10 % 5 == 0 → "factor"
  (
    "5 10\n0 0\n",
    "factor\n"
  ),
  # 테스트 케이스 4:
  # 여러 테스트 케이스가 주어지는 경우
  # 1) (20, 5) → 20 > 5 → "multiple"
  # 2) (5, 10) → 5 < 10 → "factor"
  # 3) (7, 7) → 두 수가 같으면 (자기자신은 약수이므로) "factor"로 처리
  (
    "20 5\n5 10\n7 7\n0 0\n",
    "multiple\nfactor\nfactor\n"
  ),
  # 테스트 케이스 5:
  # 1) (3, 1): 3 > 1 → "multiple"
  # 2) (1, 3): 1 < 3 → "factor"
  # 3) (4, 2): 4 > 2 → "multiple"
  # 4) (2, 4): 2 < 4 → "factor"
  (
    "3 1\n1 3\n4 2\n2 4\n0 0\n",
    "multiple\nfactor\nmultiple\nfactor\n"
  ),
  # 테스트 케이스 6:
  # 서로 약수 관계가 아닌 경우 → 모두 "neither"
  # 1) (4, 3), 2) (3, 4), 3) (8, 3), 4) (3, 8)
  (
    "4 3\n3 4\n8 3\n3 8\n0 0\n",
    "neither\nneither\nneither\nneither\n"
  ),
  # 테스트 케이스 7:
  # 1) (10, 2): 10 > 2 → "multiple"
  # 2) (2, 10): 2 < 10 → "factor"
  # 3) (6, 3): 6 > 3 → "multiple"
  # 4) (3, 6): 3 < 6 → "factor"
  (
    "10 2\n2 10\n6 3\n3 6\n0 0\n",
    "multiple\nfactor\nmultiple\nfactor\n"
  ),
  # 테스트 케이스 8:
  # 두 케이스 모두 같은 수일 때
  # 1) (12, 12) → "factor"
  # 2) (9, 9) → "factor"
  (
    "12 12\n9 9\n0 0\n",
    "factor\nfactor\n"
  ),
  # 테스트 케이스 9:
  # 1) (8, 4): 8 > 4 → "multiple"
  # 2) (4, 8): 4 < 8 → "factor"
  # 3) (8, 6): 관계 없음 → "neither"
  # 4) (6, 8): 관계 없음 → "neither"
  (
    "8 4\n4 8\n8 6\n6 8\n0 0\n",
    "multiple\nfactor\nneither\nneither\n"
  ),
  # 테스트 케이스 10:
  # 1) (100, 10): 100 > 10 → "multiple"
  # 2) (10, 100): 10 < 100 → "factor"
  # 3) (21, 7): 21 > 7 → "multiple"
  # 4) (7, 21): 7 < 21 → "factor"
  # 5) (13, 13): 같으므로 → "factor"
  (
    "100 10\n10 100\n21 7\n7 21\n13 13\n0 0\n",
    "multiple\nfactor\nmultiple\nfactor\nfactor\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
