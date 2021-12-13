# 숫자와 문자로 분리
# 분리해서 따로따로 list에 저장
# 모든 경우에수에 맞게 순열을 짜서 계산, max값 도출

visit = [0 for i in range(3)]
formula = ["+", "-", "*"]
priority = []


# 계산하는 함수
def calculator(a, b, p):
    if p == "+":
        return a + b
    elif p == "-":
        return a - b
    else:
        return a * b


def dfs(idx, temp):
    global visit, priority

    if idx == 3:
        priority.append(temp[:])
        return

    for i in range(3):
        if visit[i] == 1:
            continue
        visit[i] = 1
        temp.append(formula[i])
        dfs(idx + 1, temp)
        temp.pop()
        visit[i] = 0


def solution(expression):
    answer = 0
    formula_list = []
    num_list = []
    slice_idx = 0

    # 문자와 숫자를 분리합니다
    for i in range(len(expression)):
        if expression[i] in formula:
            formula_list.append(expression[i])
            num_list.append(int(expression[slice_idx:i]))
            slice_idx = i + 1
        # 마지막 숫자는 위의 if문으로 걸러낼 수 없어

    num_list.append(int(expression[slice_idx:]))

    # 순열로 연산자의 우선순위를 결정, 모두 더해서 abs(max) 값을 도출하자
    dfs(0, [])

    for prior in priority:
        temp_formula = formula_list[:]
        temp_num = num_list[:]
        for p in prior:
            i = 0
            while (i < len(temp_formula)):
                if p == temp_formula[i]:
                    num1 = temp_num[i]
                    num2 = temp_num.pop(i + 1)
                    temp_num[i] = calculator(num1, num2, p)
                    temp_formula.pop(i)
                    i -= 1
                i += 1
        if abs(temp_num[0]) > answer:
            answer = abs(temp_num[0])

    return answer