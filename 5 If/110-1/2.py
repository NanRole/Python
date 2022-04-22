attack = input()
hit = eval(input())
index = attack.find(' ')
A = attack[:index] # 發球方
if A == 'Right':
    B = 'Left'
else:
    B == 'Right'

if hit % 2 == 1:
    print(B, 'player win!')
else:
    print(A, 'player win!')