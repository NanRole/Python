score = eval(input())
if score > 100 or score < 0:
    print('Error')
elif score >= 90: # 0 ~ 100 -> 90 ~ 100
    print('A+')
elif score >= 85: # 85 ~ 89
    print('A')
elif score >= 80:
    print('A-')
elif score >= 77:
    print('B+')
elif score >= 73:
    print('B')
elif score >= 70:
    print('B-')
elif score >= 67:
    print('C+')
elif score >= 63:
    print('C')
elif score >= 60:
    print('C-')
elif score >= 50:
    print('D')
else:
    print('E')