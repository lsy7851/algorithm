from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
    # 테스트 케이스 1:
    # "55-50+40" → 55 - (50+40) = 55 - 90 = -35
    (
        "55-50+40\n",
        "-35\n"
    ),
    # 테스트 케이스 2:
    # "10+20+30+40" → 음수가 없으므로 모두 더함 = 100
    (
        "10+20+30+40\n",
        "100\n"
    ),
    # 테스트 케이스 3:
    # "00009-00009" → 9 - 9 = 0 (숫자에 앞의 0이 있음)
    (
        "00009-00009\n",
        "0\n"
    ),
    # 테스트 케이스 4:
    # "55-50+40-30+20-10"
    # 그룹별: "55" , "50+40" , "30+20" , "10"
    # 계산: 55 - 90 - 50 - 10 = -95
    (
        "55-50+40-30+20-10\n",
        "-95\n"
    ),
    # 테스트 케이스 5:
    # 단일 숫자 "12345" → 결과는 12345 그대로
    (
        "12345\n",
        "12345\n"
    ),
    # 테스트 케이스 6:
    # "1+2+3-4+5+6"
    # 그룹별: "1+2+3" = 6, "4+5+6" = 15 → 결과: 6 - 15 = -9
    (
        "1+2+3-4+5+6\n",
        "-9\n"
    ),
    # 테스트 케이스 7:
    # "10-20-30-40" → 그룹별: "10", "20", "30", "40"
    # 결과: 10 - 20 - 30 - 40 = -80
    (
        "10-20-30-40\n",
        "-80\n"
    ),
    # 테스트 케이스 8:
    # "10+10-5+5-15+10+10"
    # 분리: 그룹0: "10+10" = 20, 그룹1: "5+5" = 10, 그룹2: "15+10+10" = 35
    # 결과: 20 - 10 - 35 = -25
    (
        "10+10-5+5-15+10+10\n",
        "-25\n"
    ),
    # 테스트 케이스 9:
    # "50+50-50+50-50+50-50+50"
    # 분리: 그룹0: "50+50" = 100, 그룹1: "50+50" = 100, 그룹2: "50+50" = 100, 그룹3: "50+50" = 100
    # 결과: 100 - 100 - 100 - 100 = -200
    (
        "50+50-50+50-50+50-50+50\n",
        "-200\n"
    ),
    # 테스트 케이스 10:
    # "1+2+3+4-5-6+7+8-9+10-11+12+13-14+15"
    # 분리:
    # 그룹0: "1+2+3+4" = 10
    # 그룹1: "5" = 5
    # 그룹2: "6+7+8" = 21
    # 그룹3: "9+10" = 19
    # 그룹4: "11+12+13" = 36
    # 그룹5: "14+15" = 29
    # 결과: 10 - 5 - 21 - 19 - 36 - 29 = -100
    (
        "1+2+3+4-5-6+7+8-9+10-11+12+13-14+15\n",
        "-100\n"
    ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
