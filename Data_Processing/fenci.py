# 分词并写进csv
import jieba
import csv

# source = open(r'C:\Users\Cecilia\Desktop\区县.txt', 'r', encoding='utf-8')
# for name in source:
#     # seg_list = jieba.cut(name) # 默认是精确模式
#     #
#     # print(",".join(seg_list))
#     # str = "我是一个中国人"
#     seg_list = jieba.cut(name) # 搜索引擎模式
#     print(",".join(seg_list), end =" ")

file_object2=open(r'C:\Users\Cecilia\Desktop\分词.csv').read().split('\n')  #一行行的读取内容
Rs2=[] #建立存储分词的列表
for i in range(len(file_object2)):
    result=[]
    seg_list = jieba.cut(file_object2[i])
    for w in seg_list :#读取每一行分词
        result.append(w)
    Rs2.append(result)#将该行分词写入列表形式的总分词列表
#写入CSV
file=open(r'C:\\Users\\Cecilia\\Desktop\\结果.csv','w',newline='')
writer = csv.writer(file)#定义写入格式
writer.writerows(Rs2)#按行写入
#file.write(str(Rs))

file.close()