while True:
    s = input()
    if s == '0':
        break
    num, char = int(s[:-1]), s[-1]
    for i in range(1, num+1): # 1 ~ num
        print(num * char)
    print()