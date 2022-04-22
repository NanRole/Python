import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

year = ['2021上半年', '2020', '2019', '2018', '2017', '2016', '2015']
korea = [3.9, -1.9, 2.0, 2.9, 3.2, 2.9, 2.8]
taiwan = [8.34, 3.11, 2.96, 2.79, 3.31, 2.17, 1.47]
hongkong = [7.8, -6.1, -1.2, 2.8, 3.8, 2.2, 2.4]
singapore = [7.7, -5.4, 0.7, 3.4, 4.3, 3.2, 3.0]
year.reverse()
korea.reverse()
taiwan.reverse()
hongkong.reverse()
singapore.reverse()
plt.plot(year, korea, '*-', label='Korea')
plt.plot(year, taiwan, '-.', label='Taiwan')
plt.plot(year, hongkong, 'x-', label='Hongkong')
plt.plot(year, singapore, '--', label='Singapore')
plt.legend()
plt.ylim(-8, 10)
plt.title('410723001')