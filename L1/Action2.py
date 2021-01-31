import numpy as np
import pandas as pd
data = {'Chinese': [66, 95, 93, 90,80], 'Math': [30, 98, 96, 77, 90], 'English': [65, 85, 92, 88, 90]}
df = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])

print('成绩单：')
print(df)
print()

# 语文成绩统计
chinese = df['Chinese']
print('语文成绩统计：')
print('语文平均分',chinese.mean())
print('语文最低分',chinese.min())
print('语文最高分',chinese.max())
print('语文方差%.2f'%chinese.var())
print('语文标准差%.2f'%chinese.std())
print()
# 数学成绩统计
math = df['Math']
print('数学成绩统计：')
print('数学平均分',math.mean())
print('数学最低分',math.min())
print('数学最高分',math.max())
print('数学方差%.2f'%math.var())
print('数学标准差%.2f'%math.std())
print()
# 英语成绩统计
english = df['English']
print('英语成绩统计：')
print('英语平均分',english.mean())
print('英语最低分',english.min())
print('英语最高分',english.max())
print('英语方差%.2f'%english.var())
print('英语标准差%.2f'%english.std())
print()

#Pandas直接输出统计
print('成绩统计：')
print(df.describe())
print()

#成绩排名
df1=df
df1['Sum']=''
df1['Sum']=df.sum(1)
df1=df1.sort_values('Sum',ascending=False)
print('成绩排名：')
print(df1)