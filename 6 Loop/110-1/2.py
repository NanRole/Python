total = count = 0
flag = True
while True:
    value = eval(input())
    if value == -1:
        if count == 0:
            print(0.0)
            flag = False
        break
    total += value
    count += 1
if flag:
    print(total / count)