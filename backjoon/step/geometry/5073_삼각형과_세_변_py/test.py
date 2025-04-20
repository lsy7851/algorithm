from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1. 단일 Equilateral
  (
    "3 3 3\n"
    "0 0 0\n",
    "Equilateral\n"
  ),
  # 2. 단일 Scalene
  (
    "3 4 5\n"
    "0 0 0\n",
    "Scalene\n"
  ),
  # 3. 단일 Invalid (1+2=3)
  (
    "1 2 3\n"
    "0 0 0\n",
    "Invalid\n"
  ),
  # 4. 단일 Isosceles
  (
    "2 2 3\n"
    "0 0 0\n",
    "Isosceles\n"
  ),
  # 5. 여러 줄: Equilateral, Scalene, Invalid
  (
    "3 3 3\n"
    "3 4 5\n"
    "1 1 2\n"
    "0 0 0\n",
    "Equilateral\n"
    "Scalene\n"
    "Invalid\n"
  ),
  # 6. 순서 뒤섞인 테스트: Isosceles, Scalene, Invalid
  (
    "5 3 5\n"
    "6 10 7\n"
    "10 10 20\n"
    "0 0 0\n",
    "Isosceles\n"
    "Scalene\n"
    "Invalid\n"
  ),
  # 7. 작은 값 테스트: Equilateral, Invalid, Isosceles
  (
    "1 1 1\n"
    "2 2 4\n"
    "5 5 9\n"
    "0 0 0\n",
    "Equilateral\n"
    "Invalid\n"
    "Isosceles\n"
  ),
  # 8. 큰 값 테스트: Equilateral, Isosceles, Invalid
  (
    "1000000 1000000 1000000\n"
    "999999 1000000 999999\n"
    "1 1000000 500000\n"
    "0 0 0\n",
    "Equilateral\n"
    "Isosceles\n"
    "Invalid\n"
  ),
  # 9. 모두 Scalene (순서 다양)
  (
    "4 2 3\n"
    "4 3 2\n"
    "2 4 3\n"
    "0 0 0\n",
    "Scalene\n"
    "Scalene\n"
    "Scalene\n"
  ),
  # 10. 복합 테스트
  # 7 7 7 → Equilateral
  # 7 10 5 → Scalene
  # 10 5 7 → Scalene
  # 7 5 10 → Scalene
  # 4 4 8 → Invalid (4+4=8)
  # 9 4 5 → Invalid (4+5=9)
  (
    "7 7 7\n"
    "7 10 5\n"
    "10 5 7\n"
    "7 5 10\n"
    "4 4 8\n"
    "9 4 5\n"
    "0 0 0\n",
    "Equilateral\n"
    "Scalene\n"
    "Scalene\n"
    "Scalene\n"
    "Invalid\n"
    "Invalid\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
