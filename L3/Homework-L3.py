import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering


data = pd.read_csv('car_data.csv', encoding='gbk')
# print(data)
train_x = data[["地区", "人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]
print(train_x.columns)
train_x.columns = ['Area', 'GDP', 'Urban_ratio', 'Consume_index', 'Holding_per_Hundred']
print(train_x.columns)

# Data Preprocessing
le = LabelEncoder()
train_x_old = train_x
train_x['Area'] = le.fit_transform(train_x['Area'])


min_max_scaler=MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('tmp.csv', index=False)

### 使用KMeans聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("customer_cluster_result.csv",index=False)


sse = []
for k in range(1, 11):
    # kmeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

plt.figure()
model = AgglomerativeClustering(linkage='ward', n_clusters=3)
y = model.fit_predict(train_x)
print(y)
linkage_matrix = ward(train_x)
#train_x['Area'] = le.inverse_transform(train_x['Area'])
dendrogram(linkage_matrix)
plt.show()
