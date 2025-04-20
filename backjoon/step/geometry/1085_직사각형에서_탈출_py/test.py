from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1) 내 위치가 (1, 1), 직사각형이 5×5 → min(1,1,4,4) = 1
  (
    "1 1 5 5\n",
    "1\n"
  ),
  # 2) 내 위치가 (0, 3), 직사각형이 10×4 → min(0,3,10,1) = 0
  (
    "0 3 10 4\n",
    "0\n"
  ),
  # 3) 내 위치가 (5, 5), 직사각형이 10×10 → min(5,5,5,5) = 5
  (
    "5 5 10 10\n",
    "5\n"
  ),
  # 4) 내 위치가 (7, 2), 직사각형이 9×8 → min(7,2,2,6) = 2
  (
    "7 2 9 8\n",
    "2\n"
  ),
  # 5) 내 위치가 (3, 6), 직사각형이 7×6 → min(3,6,4,0) = 0
  (
    "3 6 7 6\n",
    "0\n"
  ),
  # 6) 내 위치가 (100, 50), 직사각형이 200×100 → min(100,50,100,50) = 50
  (
    "100 50 200 100\n",
    "50\n"
  ),
  # 7) 내 위치가 (1, 10), 직사각형이 100×20 → min(1,10,99,10) = 1
  (
    "1 10 100 20\n",
    "1\n"
  ),
  # 8) 내 위치가 (25, 75), 직사각형이 100×100 → min(25,75,75,25) = 25
  (
    "25 75 100 100\n",
    "25\n"
  ),
  # 9) 내 위치가 (0, 0), 직사각형이 1×1 → min(0,0,1,1) = 0
  (
    "0 0 1 1\n",
    "0\n"
  ),
  # 10) 내 위치가 (2147483646, 1), 직사각형이 2147483647×3
  #    → min(2147483646,1,1,2) = 1
  (
    "2147483646 1 2147483647 3\n",
    "1\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
