# 數值趨勢圖
import matplotlib.pyplot as plt

koraz = []
student_id = '410723001'
n = int(student_id[-2:])
if n < 10: n += 10
n_copy = n
while n != 1: # 只要n不等於1 就持續做...
    koraz.append(n)
    if n % 2 == 1: # 當n是奇數
        n = n * 3 + 1
    else: # 當n是偶數
        n = n // 2
koraz.append(1)
x = list(range(len(koraz)))
plt.plot(x, koraz, color='orange', label="n = "+str(n_copy))
plt.title(student_id)
plt.xlabel('Steps')
plt.ylabel('n value for each step')
plt.legend()
plt.show()

# 步驟趨勢圖
import matplotlib.pyplot as plt

student_id = '410723001'
n = int(student_id[-2:])
if n < 10: n += 10
n_copy = n
x = range(1, n_copy+1)
counts = []
for n in x: # 讓n由1跑到100
    count = 0
    while n != 1: # 只要n不等於1 就持續做...
        count += 1
        if n % 2 == 1: # 當n是奇數
            n = n * 3 + 1
        else: # 當n是偶數
            n = n / 2
    counts.append(count)
plt.plot(x, counts, color='blue', label='Positive Integer Step Number Trend')
plt.title(student_id)
plt.xlabel('n')
plt.ylabel('step pre number')
plt.legend()
plt.show()