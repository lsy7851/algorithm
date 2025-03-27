from solution_node import solve as solve_node
from solution_array import solve as solve_array
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: 원이 하나이면 그룹은 1개
  (
    "1\n1\n0 0 1\n",
    "1\n"
  ),
  # 테스트 케이스 2: 2개의 원이 서로 멀리 떨어져 있으므로 각자 다른 그룹
  (
    "1\n2\n0 0 1\n5 0 1\n",
    "2\n"
  ),
  # 테스트 케이스 3: 2개의 원이 딱 맞게 접하여 같은 그룹
  (
    "1\n2\n0 0 2\n4 0 2\n",
    "1\n"
  ),
  # 테스트 케이스 4: 3개의 원 중 앞의 두는 서로 접하고, 세 번째는 떨어져 있으므로 그룹 2개
  (
    "1\n3\n0 0 1\n2 0 1\n5 0 1\n",
    "2\n"
  ),
  # 테스트 케이스 5: 4개의 원을 일렬로 배치하여 연쇄적으로 모두 연결되어 있으므로 그룹 1개
  (
    "1\n4\n0 0 1\n2 0 1\n4 0 1\n6 0 1\n",
    "1\n"
  ),
  # 테스트 케이스 6: 5개의 원 – 두 그룹으로 나뉨
  #  그룹1: (0,0,1)와 (1,1,1) (서로 겹침)
  #  그룹2: (10,10,2)와 (12,10,2) (서로 접함), 그리고 (20,20,1)는 단독 그룹
  (
    "1\n5\n0 0 1\n1 1 1\n10 10 2\n12 10 2\n20 20 1\n",
    "3\n"
  ),
  # 테스트 케이스 7: 6개의 원이 모두 같은 중심에 있는 경우
  (
    "1\n6\n0 0 5\n0 0 3\n0 0 1\n0 0 4\n0 0 2\n0 0 6\n",
    "1\n"
  ),
  # 테스트 케이스 8: 6개의 원을 일렬로 배치 (간격 1)하여 모두 서로 충분히 겹쳐 한 그룹이 됨
  (
    "1\n6\n0 0 1\n1 0 1\n2 0 1\n3 0 1\n4 0 1\n5 0 1\n",
    "1\n"
  ),
  # 테스트 케이스 9: 7개의 원 – 좌측 3개는 연결되고, 우측 4개 중 3개는 연결되나 마지막 원은 단독
  (
    "1\n7\n0 0 2\n3 0 2\n6 0 2\n20 20 1\n21 20 1\n22 20 1\n25 20 1\n",
    "3\n"
  ),
  # 테스트 케이스 10 (성능 테스트용): N을 충분히 크게 하여 1000개의 원을 일렬로 배치
  # 각 원은 (2*i, 0) 위치에 있으며 반지름은 1로, 인접 원과 거리가 2로 딱 맞아 접하게 되므로 모두 연결되어 1개의 그룹.
  (
    "1\n1000\n" + "\n".join(f"{2 * i} 0 1" for i in range(1000)) + "\n",
    "1\n"
  ),
]


def test_node():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve_node)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"


def test_array():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve_array)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
