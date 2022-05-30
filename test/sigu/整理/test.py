import unittest
import pandas as pd


data_file = 'zhengti01.csv'                       # 文件路径
df = pd.read_csv(data_file, encoding='UTF-8')   # 读取csv文件为datafile，编码为utf-8
texts = df['text'].tolist()
i = 0
for text in texts[0:100]:
    i += 1
    print(text)
print(i)