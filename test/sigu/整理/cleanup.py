import pandas as pd
import re


def tihuan(text):
    # 函数功能替换字符中字符
    t = re.sub(' ', '', text)  # 此函数三个参数，第一个为匹配的符号，第二个替换的符号，第三个字符串
    t = re.sub('，', '', t)
    t = re.sub('。', '', t)
    t = re.sub(',', '', t)
    t = re.sub('”', '', t)
    t = re.sub('《', '', t)
    t = re.sub('》', '', t)
    t = re.sub('、', '', t)
    t = re.sub('）', '', t)
    t = re.sub('（', '', t)
    t = re.sub('“', '', t)
    t = re.sub('；', '', t)
    t = re.sub('●', '', t)
    t = re.sub('：', '', t)
    t = re.sub('safehoo.com', '', t)
    t = re.sub(r'\n', '', t)
    t = t.strip().replace(' ', '').replace('\n', '').replace('\r', '')
    t = ''.join(t.split())  # 以空格切片字符串，然后再以''拼接起来
    return t


data_file = 'zhengti_yuan.csv'  # 文件路径
df = pd.read_csv(data_file, encoding='UTF-8')  # 读取csv文件为datafile，编码为utf-8
df['text'] = df['text'].apply(tihuan)  # apply应用参数内的函数
# df.to_csv('zhengti01.csv', index = False)       # 保存为csv文件
texts = df['text'].tolist()
i = 0
for text in texts[0:100]:
    i += 1
    print(text)
print(i)
