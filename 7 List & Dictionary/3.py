mersenne = {}
while True:
    n = int(input())
    if n == -1:
        break
    mersenne[n] = 2 ** n - 1
print(mersenne)