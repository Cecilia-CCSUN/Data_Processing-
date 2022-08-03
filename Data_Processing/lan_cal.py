# 匹配方言
#coding=utf-8
import csv

import pandas
import numpy

f1 = open(r'C:\Users\Cecilia\Desktop\2022-07资料\数据\file1.csv', 'r')
f1_reader = csv.reader(f1, delimiter=',')



for row in f1_reader:
    num = []

    if '、' in row[8]:
        print("普通话")



            # Use values to copy the color value to file1.csv
    else :
        f2 = open(r'C:\Users\Cecilia\Desktop\2022-07资料\数据\方言.csv', 'r')
        f2_reader = csv.reader(f2, delimiter=',')
        sum = -1
        for line in f2_reader:
            if row[8] in (
                    "郊区", "桥西区",  "长安区", "新华区", "鼓楼区", "通州区", "永定区", "南山区", "向阳区", "西安区", "江夏区", "青山区", "城关区",
                    "靖远县",
                    "鼎城区", "永定区", "宁远县", "新田县", "会同县", "龙华区", "城区", "铁东区", "铁西区", "东辽县", "通化县", "城中区", "钟山区", "余庆县",
                    "天柱县",
                    "施秉县", "龙华区", "海州区", "普陀区", "西湖区", "东区", "市中区", "犍为县", "洪雅县", "会理县", "河东区", "新城区", "尼玛县", "噶尔县",
                    "东区",
                    "市中区", "江北区", "新城区"):
                if row[9] == line[2]:
                    print(line[1])
                    break


            else:
                if row[8] == line[0]:
                    print(line[1])
                    break



