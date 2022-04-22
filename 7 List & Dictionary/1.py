li = []
while True:
    n = eval(input())
    if n == 0:
        break
    li.append(n)
li.sort(reverse=True)
print(li)