import pandas as pd

my_id = '410723001'
start = int(my_id[-1])
if start == 0:
    start = 10

# Method 1
# datas = pd.read_csv('timelist.csv')
# student_ids = datas["學號"]
# hours = datas["本月時數"]
# salarys = []
# for i in range(len(hours)):
#     if str(student_ids[i])[0] == '4':
#         salarys.append(180 * hours[i])
#     else:
#         salarys.append(200 * hours[i])
# datas["薪資"] = salarys
# datas[start-1:].to_csv(my_id+'.csv', index=False, encoding='utf_8_sig')

# Method 2
fp1 = open('timelist.csv', 'r', encoding='utf-8')
fp2 = open(my_id+'.csv', 'w')
datas = fp1.readlines()
header = True
count = 0
for data in datas:
    data = data.rstrip('\n')
    if header:
        fp2.write(data+',薪資\n')
        header = False
    else:
        count += 1
        if count >= start:
            comma = data.split(',')
            student_id, hour = comma[2], int(comma[3])
            if student_id[0] == '4':
                fp2.write(data+','+str(180 * hour)+'\n')
            else:
                fp2.write(data+','+str(200 * hour)+'\n')
fp1.close()
fp2.close()
