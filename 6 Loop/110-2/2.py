sum = count = 0
while True:
    num = eval(input())
    if num == -1:
        if count == 0:
            print(0.0)
        else:
            print(sum / count)
        break
    if num > 0:
        sum += num # sum = sum + num
        count += 1