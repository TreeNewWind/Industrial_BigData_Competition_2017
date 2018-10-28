#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 可优化方向：
# 1. 数据归一化处理
# 2. 网格搜索寻找SVM最优参数(C&gamma)
# 3. 绘制roc曲线以评价模型

import pickle
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


batch = str(21)
data = pd.read_csv('./processed/%s_avg10_lowPower_data.csv' %batch)
X = data[['wind_speed', 'power']]
y = data['frozen']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=5000, random_state=1)

model = SVC(kernel='rbf', C=1E10)
model.fit(X_train, y_train)
ymodel = model.predict(X_test)
print('验证集准确率：%0.3f\n\n' %accuracy_score(ymodel, y_test))

with open('models/svm_model_%s.pkl' %batch, 'wb') as f:
    pickle.dump(model, f)

# pickle写入方法：
# 1. pickle.dump()
#
# with open('test.txt', 'wb') as f:
#     pickle.dump(sth, f)
#
# 2. pickle.dumps()
#
# s = pickle.dumps(sth)
# with open('test.txt', 'wb') as f:
#     f.write(s)