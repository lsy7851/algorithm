from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1) 60, 60, 60 → 모두 같은 각 → Equilateral
  (
    "60\n"
    "60\n"
    "60\n",
    "Equilateral\n"
  ),
  # 2) 30, 60, 90 → 세 각이 모두 다름, 합 = 180 → Scalene
  (
    "30\n"
    "60\n"
    "90\n",
    "Scalene\n"
  ),
  # 3) 90, 45, 45 → 두 각이 같음, 합 = 180 → Isosceles
  (
    "90\n"
    "45\n"
    "45\n",
    "Isosceles\n"
  ),
  # 4) 120, 30, 30 → 두 각이 같음, 합 = 180 → Isosceles
  (
    "120\n"
    "30\n"
    "30\n",
    "Isosceles\n"
  ),
  # 5) 100, 40, 40 → 두 각이 같음, 합 = 180 → Isosceles
  (
    "100\n"
    "40\n"
    "40\n",
    "Isosceles\n"
  ),
  # 6) 58, 59, 63 → 세 각이 모두 다름, 합 = 180 → Scalene
  (
    "58\n"
    "59\n"
    "63\n",
    "Scalene\n"
  ),
  # 7) 50, 60, 70 → 세 각이 모두 다름, 합 = 180 → Scalene
  (
    "50\n"
    "60\n"
    "70\n",
    "Scalene\n"
  ),
  # 8) 100, 50, 40 → 합 = 190 ≠ 180 → Error
  (
    "100\n"
    "50\n"
    "40\n",
    "Error\n"
  ),
  # 9) 60, 60, 59 → 합 = 179 ≠ 180 → Error
  (
    "60\n"
    "60\n"
    "59\n",
    "Error\n"
  ),
  # 10) 10, 10, 10 → 합 = 30 ≠ 180 → Error
  (
    "10\n"
    "10\n"
    "10\n",
    "Error\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
