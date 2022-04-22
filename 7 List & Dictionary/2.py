while True:
    fib = [0, 1]
    n = eval(input())
    if n == 0:
        print([0])
        continue
    if n == -1:
        break
    for i in range(n-1):
        fib.append(fib[-1] + fib[-2])
    print(fib)