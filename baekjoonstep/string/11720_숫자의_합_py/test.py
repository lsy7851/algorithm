from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('1\n1', '1\n'),
  ('5\n54321', '15\n'),
  ('25\n7000000000000000000000000', '7\n'),
  ('11\n10987654321', '46\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
