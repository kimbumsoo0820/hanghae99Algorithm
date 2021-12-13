num = int(input())

for loop in range(num):
    check = input()
    ls = list(check)
    sum = 0

    for  i in ls:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    if sum == 0:
        print('YES')