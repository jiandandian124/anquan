from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
import pandas as pd


all_data = pd.read_csv("zhengti_fenci_fenlei.csv")
train_data, test_data = train_test_split(all_data, train_size=0.9, test_size=0.1)
print(train_data)
print(test_data)

train_data.to_csv("zhengti_train.csv",index=False)
test_data.to_csv("zhengti_test.csv",index=False)
