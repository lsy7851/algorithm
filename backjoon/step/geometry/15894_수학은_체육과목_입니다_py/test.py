from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # n=1 → 4×1 = 4
  (
    "1\n",
    "4\n"
  ),
  # n=2 → 4×2 = 8
  (
    "2\n",
    "8\n"
  ),
  # n=3 → 4×3 = 12
  (
    "3\n",
    "12\n"
  ),
  # n=10 → 4×10 = 40
  (
    "10\n",
    "40\n"
  ),
  # n=100 → 4×100 = 400
  (
    "100\n",
    "400\n"
  ),
  # n=123456789 → 4×123456789 = 493827156
  (
    "123456789\n",
    "493827156\n"
  ),
  # n=500000000 → 4×500000000 = 2000000000
  (
    "500000000\n",
    "2000000000\n"
  ),
  # n=777777777 → 4×777777777 = 3111111108
  (
    "777777777\n",
    "3111111108\n"
  ),
  # n=999999999 → 4×999999999 = 3999999996
  (
    "999999999\n",
    "3999999996\n"
  ),
  # n=1000000000 → 4×1000000000 = 4000000000
  (
    "1000000000\n",
    "4000000000\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
