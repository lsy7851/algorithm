from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1) N=3, 최소한의 꼭짓점 세 점
  # points: (0,0),(0,1),(1,0) → width=1, height=1 → area=1
  (
    "3\n"
    "0 0\n"
    "0 1\n"
    "1 0\n",
    "1\n"
  ),
  # 2) N=4, 정확한 사각형 네 꼭짓점
  # points: (0,0),(3,0),(0,2),(3,2) → width=3, height=2 → area=6
  (
    "4\n"
    "0 0\n"
    "3 0\n"
    "0 2\n"
    "3 2\n",
    "6\n"
  ),
  # 3) N=4, 음수 좌표 포함
  # points: (-1,-1),(-1,1),(1,-1),(1,1) → width=2, height=2 → area=4
  (
    "4\n"
    "-1 -1\n"
    "-1 1\n"
    "1 -1\n"
    "1 1\n",
    "4\n"
  ),
  # 4) N=6, 중복 및 내부점 포함
  # points: (0,0),(5,0),(5,5),(0,5),(3,3),(5,0) → width=5, height=5 → area=25
  (
    "6\n"
    "0 0\n"
    "5 0\n"
    "5 5\n"
    "0 5\n"
    "3 3\n"
    "5 0\n",
    "25\n"
  ),
  # 5) N=3, 가로 폭이 0인 경우
  # points: (2,1),(2,3),(2,5) → width=0, height=4 → area=0
  (
    "3\n"
    "2 1\n"
    "2 3\n"
    "2 5\n",
    "0\n"
  ),
  # 6) N=5, 매우 큰 좌표
  # points: (100000,200000),(100000,100000),(200000,100000),(200000,200000),(150000,150000)
  # → width=100000, height=100000 → area=10000000000
  (
    "5\n"
    "100000 200000\n"
    "100000 100000\n"
    "200000 100000\n"
    "200000 200000\n"
    "150000 150000\n",
    "10000000000\n"
  ),
  # 7) N=7, 혼합 음수·양수
  # minX=-5, maxX=10, minY=-6, maxY=4 → width=15, height=10 → area=150
  (
    "7\n"
    "-5 4\n"
    "0 4\n"
    "10 4\n"
    "10 -6\n"
    "0 -6\n"
    "-5 -6\n"
    "3 0\n",
    "150\n"
  ),
  # 8) N=3, 폭과 높이가 같은 간단한 정사각형
  # points: (10,10),(20,10),(10,20) → width=10, height=10 → area=100
  (
    "3\n"
    "10 10\n"
    "20 10\n"
    "10 20\n",
    "100\n"
  ),
  # 9) N=4, 대각선상 점들
  # points: (1,1),(2,2),(3,3),(4,4) → width=3, height=3 → area=9
  (
    "4\n"
    "1 1\n"
    "2 2\n"
    "3 3\n"
    "4 4\n",
    "9\n"
  ),
  # 10) N=10, 임의의 분포
  # minX=-10, maxX=10, minY=-2, maxY=7 → width=20, height=9 → area=180
  (
    "10\n"
    "-10 0\n"
    "10 0\n"
    "-10 5\n"
    "10 5\n"
    "-5 3\n"
    "5 -2\n"
    "-8 -1\n"
    "8 6\n"
    "0 7\n"
    "-2 4\n",
    "180\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
