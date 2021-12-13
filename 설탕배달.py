inp = int(input())
# inp = 10
carry_box = 0;

while True:
    if (inp%5) == 0:
        carry_box= carry_box + (inp//5)
        print(carry_box)
        break
    inp = inp-3
    carry_box +=1
    if inp < 0:
        print(-1)
        break


