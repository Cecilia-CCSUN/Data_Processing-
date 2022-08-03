# 匹配非物质文化遗产名录
#coding=utf-8
import csv
import pandas

import numpy as np

f1 = open(r'C:\Users\Cecilia\Desktop\2022-07资料\数据\file1.csv', 'r')
f1_reader = csv.reader(f1, delimiter=',')

i = 0
j = 0
sum = 0.

for row in f1_reader:
    num1 = []
    num2 = []
    count = 0
    if '、' in row[8]:
        row_list = row[8].split('、')
        for k in row_list:
            f2 = open(r'C:\Users\Cecilia\Desktop\2022-07资料\数据\file3.csv', encoding='utf-8')
            f2_reader = csv.reader(f2, delimiter=',')
            for line in f2_reader:
                if k in ("郊区" ,"桥西区"  ,"长安区" ,"新华区" ,"鼓楼区" ,"通州区" , "永定区" , "南山区" ,"向阳区" , "西安区" , "江夏区" ,"青山区", "城关区" , "靖远县" , "鼎城区"  , "永定区" , "宁远县" , "新田县" ,"会同县" ,"龙华区" ,"城区" ,"铁东区" ,"铁西区" , "东辽县" ,"通化县" ,"城中区" , "钟山区" ,"余庆县" , "天柱县" , "施秉县" ,"龙华区" ,"海州区" , "普陀区" , "西湖区" ,"东区" ,"市中区" , "犍为县" ,"洪雅县" , "河东区" ,"新城区" , "尼玛县" , "噶尔县" ,"东区" , "市中区", "江北区" , "新城区"):
                    if row[9] == line[23]:
                        num1.append(line[3])
                        count+=1
                    elif row[7] == line[21]:
                        num1.append(line[3])
                        count+=1
                    elif row[6] == line[20]:
                        num1.append(line[3])
                        count+=1

                else:
                    if k == line[22]:
                        num1.append(line[3])
                        count+=1
                    elif row[7] == line[21]:
                        count += 1
                        num1.append(line[3])
                        count += 1
                    elif row[6] == line[20]:
                        num1.append(line[3])

            f2.close
        num1 = np.unique(num1)
        print(num1)
        sum=0
            # Use values to copy the color value to file1.csv
    else :
        f2 = open(r'C:\Users\Cecilia\Desktop\2022-07资料\数据\file3.csv', encoding='utf-8')
        f2_reader = csv.reader(f2, delimiter=',')
        for line in f2_reader:
            if row[8] in ("郊区", "桥西区", "长安区", "新华区", "鼓楼区", "通州区", "永定区", "南山区", "向阳区", "西安区", "江夏区", "青山区", "城关区", "靖远县","鼎城区", "永定区", "宁远县", "新田县", "会同县", "龙华区", "城区", "铁东区", "铁西区", "东辽县", "通化县", "城中区", "钟山区", "余庆县", "天柱县", "施秉县", "龙华区", "海州区", "普陀区", "西湖区", "东区", "市中区", "犍为县", "洪雅县", "会理县", "河东区", "新城区", "尼玛县", "噶尔县", "东区", "市中区", "江北区", "新城区"):
                if row[9]==line[23]:
                    num1.append(line[3])
                    count += 1
                elif row[7] == line[21]:
                    num1.append(line[3])
                    count += 1
                elif row[6] == line[20]:
                    num1.append(line[3])
                    count += 1

            else:
                if row[8]==line[22]:
                    num1.append(line[3])
                    count += 1
                elif row[7] == line[21]:
                    num1.append(line[3])
                    count += 1
                elif row[6] == line[20]:
                    num1.append(line[3])
                    count += 1
        num1 = np.unique(num1)
        print(num1)
        sum=0

        j = j + 1

    i = i + 1
# file=open(r'C:\\Users\\Cecilia\\Desktop\\结果2.csv','w',newline='')
# writer = csv.writer(file)#定义写入格式
# writer.writerows(num1)#按行写入
# #file.write(str(Rs))
#
# file.close()
