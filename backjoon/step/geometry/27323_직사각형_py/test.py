from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1×1 = 1
  (
    "1\n"
    "1\n",
    "1\n"
  ),
  # 2×3 = 6
  (
    "2\n"
    "3\n",
    "6\n"
  ),
  # 10×20 = 200
  (
    "10\n"
    "20\n",
    "200\n"
  ),
  # 0×5 = 0
  (
    "0\n"
    "5\n",
    "0\n"
  ),
  # 100×200 = 20000
  (
    "100\n"
    "200\n",
    "20000\n"
  ),
  # 46340×46340 = 2147395600 (int 32비트 한계 내 최대 근방)
  (
    "46340\n"
    "46340\n",
    "2147395600\n"
  ),
  # 12345×6789 = 83810205
  (
    "12345\n"
    "6789\n",
    "83810205\n"
  ),
  # 1000×1000 = 1000000
  (
    "1000\n"
    "1000\n",
    "1000000\n"
  ),
  # 99999×0 = 0
  (
    "99999\n"
    "0\n",
    "0\n"
  ),
  # 2147×2147 = 4609609
  (
    "2147\n"
    "2147\n",
    "4609609\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
