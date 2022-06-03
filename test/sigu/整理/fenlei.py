import pandas as pd
import jieba


def fenlei(label):
    t = label
    if t == '交通事故':
        t = 0
    elif t == '消防事故':
        t = 1
    elif t == '矿山事故':
        t = 2
    elif t == '建筑事故':
        t = 3
    elif t == '化工事故':
        t = 4
    elif t == '特种设备':
        t = 5
    elif t == '电力事故':
        t = 6
    elif t == '机械事故':
        t = 7
    elif t == '冶金事故':
        t = 8
    else :
        t = -1

    return t




data_file = 'zhengti_fenci.csv'  # 文件路径
df = pd.read_csv(data_file, encoding='UTF-8')  # 读取csv文件为datafile，编码为utf-8
df['label'] = df['label'].apply(fenlei)  # apply应用参数内的函数
df.to_csv('zhengti_fenci_fenlei.csv', index = False)       # 保存为csv文件
labels = df['label'].tolist()
i = 0
for text in labels[0:100]:
    i += 1
    print(text)
print(i)