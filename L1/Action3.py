import numpy as np
import pandas as pd

# 读入csv
data = pd.read_csv('./car_data_analyze/car_complain.csv')
print(data)
print(data.iloc[0])

# 去除重复行
data = data.drop_duplicates()
print(data)

# 从投诉条目中分离出问题数目
data_problem_split = data['problem'].str.split(',', expand=True)

problem_count = data_problem_split
problem_count['Problem_Count'] = ''
for i in range(len(problem_count)):
    count = 0
    line = data_problem_split.iloc[i].isnull()
    for j in range(line.count() - 1):
        if not line[j]:
            count = count + 1
    problem_count['Problem_Count'][i] = count-1

#problem_count=problem_count.reset_index()
#problem_count.to_csv('car_problem_count.csv',index=False)

# 将统计出的问题数目合并到统计表里
data_concat = data.merge(data_problem_split, left_index=True, right_index=True, how='left')
print(data_concat)

# 提取需要用到的列项目
data_problem = data_concat.loc[:, [ 'brand', 'car_model','Problem_Count']]

# 替换歧义名称
data_problem.replace({'一汽-大众':'一汽大众'},inplace=True)
data_problem.to_csv('data_problem.csv',index=False)

# 以品牌为索引，分别统计问题数目和投诉计次
dg1 = data_problem.groupby('brand')['Problem_Count'].sum().sort_values(ascending=False)
print('各品牌问题总数')
print(dg1)
dg2 = data_problem['Problem_Count'].groupby(data_problem['brand']).count().sort_values(ascending=False)
print('各品牌投诉总数')
print(dg2)

# 以车型为索引，分别统计问题数目和投诉计次
dg3 = data_problem.groupby('car_model')['Problem_Count'].sum().sort_values(ascending=False)
print('各车型问题总数')
print(dg3)
dg4 = data_problem['Problem_Count'].groupby(data_problem['car_model']).count().sort_values(ascending=False)
print('各车型投诉总数')
print(dg4)

# 获取各品牌车型数目，以去重复的方式只保留第一次出现的
car_model_count = data_problem.drop_duplicates(subset=['brand','car_model'],keep='first')
print(car_model_count)

# 统计各品牌车型数目
dg = car_model_count['car_model'].groupby(car_model_count['brand']).count().sort_values(ascending=False)

print('各品牌车型数目:')
print(dg)
print()

dg7=dg.reset_index()
dg7.to_csv('count_car_model.csv',index=False)

# 统计品牌投诉次数
Brand_problem_sum = data_problem.groupby('brand')['Problem_Count'].sum()
# 统计品牌问题总数
Brand_problem_count =  data_problem['Problem_Count'].groupby(data_problem['brand']).count()
# 计算品牌平均车型
car_model_count = car_model_count['car_model'].groupby(car_model_count['brand']).count()

print('品牌平均车型投诉数目排序：')
print(round(Brand_problem_count.divide(car_model_count).sort_values(ascending=False),2))
print('品牌平均车型问题数目排序：')
print(round(Brand_problem_sum.divide(car_model_count).sort_values(ascending=False),2))
