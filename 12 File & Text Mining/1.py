# import pandas as pd

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
# datas.to_csv('410723001.csv', index=False, encoding='utf_8_sig')

fp1 = open('timelist.csv', 'r', encoding='utf-8')
fp2 = open('410723001.csv', 'w')
datas = fp1.readlines()
header = True
for data in datas:
    data = data.rstrip('\n')
    if header:
        fp2.write(data+',薪資\n')
        header = False
    else:
        comma = data.split(',')
        student_id, hour = comma[2], int(comma[3])
        if student_id[0] == '4':
            fp2.write(data+','+str(180 * hour)+'\n')
        else:
            fp2.write(data+','+str(200 * hour)+'\n')
fp1.close()
fp2.close()