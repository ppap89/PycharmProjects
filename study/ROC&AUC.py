import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize  # 将label二值化
import matplotlib.pyplot as plt

data = pd.read_csv('D:/Desktop/1/1/car.data', header=None)  # header=None没有标题
print(data.shape)
n_columns = len(data.columns)  # 获取数据集的列数
columns = ['buy', 'maintain', 'doors', 'persons', 'boot', 'safety', 'accept']
new_columns = dict(zip(np.arange(n_columns), columns))  # 将列名与整数影射
data.rename(columns=new_columns, inplace=True)  # 替换数据集中的列名columns中的值
for col in columns:
    # Categorical方法，获取list的类别，codes方法赋给每个类别对应的类别的编码值
    data[col] = pd.Categorical(data[col]).codes

x = data.loc[:, columns[:-1]]  # 得到样本特征y = data[ 'accept']#取到标签值
y = data['accept']
x, x_test, y, y_test = train_test_split(x, y, test_size=0.3)
clf = DecisionTreeClassifier(criterion='gini', max_depth=12, min_samples_split=5, max_features=5)
clf.fit(x, y)
y_hat = clf.predict(x)  # 在训练集上进行预测
print('训练集精确度:', metrics.accuracy_score(y, y_hat))  # 评估成绩
y_test_hat = clf.predict(x_test)  # 测试集预测
print('测试集精确度:', metrics.accuracy_score(y_test, y_test_hat))  # 评估绘制曲线
n_class = len(data['accept'].unique())
y_test_one_hot = label_binarize(y_test, classes=np.arange(n_class))  # 将标签值映射成one-hot编码
y_test_one_hot_hat = clf.predict_proba(x_test)  # 测试集预测分类概率

# 计算fpr ,tpr及面积
fpr, tpr, _ = metrics.roc_curve(y_test_one_hot.ravel(), y_test_one_hot_hat.ravel())
print('Micro AUC:\t', metrics.auc(fpr, tpr))  # AUC ROC意思是ROC曲线下方的面积(Area under the Curve of ROC)
print('Micro AUC(System):\t', metrics.roc_auc_score(y_test_one_hot, y_test_one_hot_hat, average='micro'))

auc = metrics.roc_auc_score(y_test_one_hot, y_test_one_hot_hat, average='macro')
print('Macro AUC:\t', auc)

plt.figure(figsize=(8, 7), dpi=80, facecolor='w')
plt.xlim((-0.01, 1.02))
plt.ylim((-0.01, 1.02))
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.plot(fpr, tpr, 'r-', lw=2, label='AUC=%.4f' % auc)
plt.legend(loc='lower right')
plt.xlabel('False Positive Rate', fontsize=14)
plt.ylabel('True Positive Rate', fontsize=14)
plt.grid(b=True, ls=':')
plt.title(u'DecisionTree ROC curve And AUC', fontsize=18)
plt.show()



test