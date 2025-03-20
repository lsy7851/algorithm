from solution import solve
from util.test_runner import run_fun_solution

from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  (
    """3
ACDKJFOWIEGHE
O
AB
""",
    """AE
OO
AB
"""
  ),
  (
    """20
Baekjoon
baekjoon
Hello
Python
algorithm
contest
developer
acmicpc
example
random
testing
pytest
solution
keyboard
monitor
laptop
desktop
internet
programming
challenge
""",
    """Bn
bn
Ho
Pn
am
ct
dr
ac
ee
rm
tg
pt
sn
kd
mr
lp
dp
it
pg
ce
"""
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
