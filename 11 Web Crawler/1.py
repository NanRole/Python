import requests

areas = {
    '安置區': 'http://faculty.ndhu.edu.tw/~aowoo-welfare/area0.html',
    '集賢區': 'http://faculty.ndhu.edu.tw/~aowoo-welfare/area1.html',
    '原住民區': 'http://faculty.ndhu.edu.tw/~aowoo-welfare/area2.html',
    '教院區': 'http://faculty.ndhu.edu.tw/~aowoo-welfare/area3.html',
    '多容區': 'http://faculty.ndhu.edu.tw/~aowoo-welfare/area4.html',
    '中途中的狗狗們': 'http://faculty.ndhu.edu.tw/~aowoo-welfare/areahome.html'
}

area = input('請輸入狗勾數量的查詢區域(安置區、集賢區、原民院區、教院區、多容區、中途中的狗狗們)：')
url = areas[area]

html = requests.get(url)
html.encoding = 'utf8'
htmlwords = html.text.splitlines()

n = 0
for words in htmlwords:
    if '性別' in words:
        n += 1
print(area, '內總共有', n, '隻狗狗 (410723001)')