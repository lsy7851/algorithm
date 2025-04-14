from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('A', '65\n'),
  ('C', '67\n'),
  ('0', '48\n'),
  ('9', '57\n'),
  ('a', '97\n'),
  ('z', '122\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
