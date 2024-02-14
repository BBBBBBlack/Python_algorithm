# 基本数据处理——缺失值、数值化
import pandas as pd

df = pd.read_csv("C:\\Users\\black\Downloads\\Wimbledon_featured_matches.csv")
df = df[df['match_id'] == '2023-wimbledon-1701']

# 将serve_width和serve_depth的缺失值删除
df.dropna(subset=['serve_width'], inplace=True)
df.dropna(subset=['serve_depth'], inplace=True)
# 将serve_width和serve_depth的值数值化
df['serve_width'] = df['serve_width'].map({'B': 1, 'BC': 2, 'BW': 3, 'C': 4, 'W': 5})
df['serve_depth'] = df['serve_depth'].map({'CTL': 1, 'NCTL': 2})

# 将return_depth缺失值和ND替换为0，D替换为1
df['return_depth'] = df['return_depth'].map({'ND': 0, 'D': 1})
df.loc[df['return_depth'].isnull(), 'return_depth'] = 0

df.drop('winner_shot_type', axis=1, inplace=True)

# 将speed_mph缺失值替换为平均值
# Carlos Alcaraz的平均发球速度
AC_avg_speed = df['speed_mph'][df['server'] == 1].dropna().sum() / df['speed_mph'][df['server'] == 1].dropna().count()
# Daniil Medvedev的平均发球速度
DM_avg_speed = df['speed_mph'][df['server'] == 2].dropna().sum() / df['speed_mph'][df['server'] == 2].dropna().count()
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 1), 'speed_mph'] = AC_avg_speed
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 2), 'speed_mph'] = DM_avg_speed

df.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\base.csv", index=False)
