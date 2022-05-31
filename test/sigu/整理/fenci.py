import pandas as pd
import jieba


def fenci(text):
    t = text
    t = jieba.lcut(t)            # 用jieba精确模式分词，得到词列表
    t = ' '.join(i for i in t)   # for遍历整个列表，然后以空格连接 i
    return t


data_file = 'zhengti_cleanup.csv'  # 文件路径
df = pd.read_csv(data_file, encoding='UTF-8')  # 读取csv文件为datafile，编码为utf-8
df['text'] = df['text'].apply(fenci)  # apply应用参数内的函数
# df.to_csv('zhengti_fenci.csv', index = False)       # 保存为csv文件
texts = df['text'].tolist()
i = 0
for text in texts[0:100]:
    i += 1
    print(text)
print(i)