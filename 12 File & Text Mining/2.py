import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft jhengHei'

datas = pd.read_html('https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85')
student_id = '410723001'
country = '國家/地區'
index = 0
for data in datas:
    if country in str(data):
        break
    index += 1
table = datas[index]
table = table[1:int(student_id[-1])+10+1]
plt.bar(table[country], list(map(int, table['确诊[a]'])))
plt.title(student_id)
plt.xlabel('國家')
plt.ylabel('人數')
plt.xticks(rotation=90)
plt.show()
