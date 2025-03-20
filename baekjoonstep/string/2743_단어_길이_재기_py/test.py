from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ("Baekjoon", "8\n"),
  ("Baekjoon", "8\n"),
  ("Hello", "5\n"),
  ("Python", "6\n"),
  ("algorithm", "9\n"),
  ("contest", "7\n"),
  ("developer", "9\n"),
  ("acmicpc", "7\n"),
  ("example", "7\n"),
  ("random", "6\n"),
  ("testing", "7\n"),
  ("pytest", "6\n"),
  ("solution", "8\n"),
  ("keyboard", "8\n"),
  ("monitor", "7\n"),
  ("laptop", "6\n"),
  ("desktop", "7\n"),
  ("internet", "8\n"),
  ("programming", "11\n"),
  ("challenge", "9\n")
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
