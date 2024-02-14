import pandas as pd


def change(data):
    data['elapsed_time'] = pd.to_datetime(data['elapsed_time'], format='%H:%M:%S')
    data.reset_index(drop=True, inplace=True)
    return data


# def divide(data):


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
AC_avg_speed = df['speed_mph'][df['server'] == 1].dropna().sum() / df['speed_mph'][df['server'] == 1].dropna().count()
# Novak Djokovic的平均发球速度
DN_avg_speed = df['speed_mph'][df['server'] == 2].dropna().sum() / df['speed_mph'][df['server'] == 2].dropna().count()
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 1), 'speed_mph'] = AC_avg_speed
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 2), 'speed_mph'] = DN_avg_speed

# 分离p1和p2的数据
columns = ['elapsed_time', 'set_no', 'game_no', 'point_no', 'sets', 'games', 'server', 'point_victor']
AC2 = pd.concat(
    [df['elapsed_time'], df['set_no'], df['game_no'], df['point_no'],
     df['p1_sets'], df['p1_games'], df['server'], df['point_victor']], axis=1)
AC2.columns = columns

# 对ND执行同样的操作
ND2 = pd.concat(
    [df['elapsed_time'], df['set_no'], df['game_no'], df['point_no'],
     df['p2_sets'], df['p2_games'], df['server'], df['point_victor']], axis=1)
ND2.columns = columns

AC2.loc[AC2['server'] == 2, 'server'] = 0
AC2['point_victor'] = AC2['point_victor'].map({1: 1, 2: 0})
ND2.loc[ND2['server'] == 1, 'server'] = 0
ND2.loc[ND2['server'] == 2, 'server'] = 1
ND2['point_victor'] = ND2['point_victor'].map({1: 0, 2: 1})

AC2 = change(AC2)
ND2 = change(ND2)

tt = pd.read_csv("/file/AC_res.csv")
AC2 = pd.concat([AC2, tt['1']], axis=1)
tt = pd.read_csv("/file/ND_res.csv")
ND2 = pd.concat([ND2, tt['1']], axis=1)
# save
AC2.to_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC2.csv", index=False)
ND2.to_csv("D:\\xxx\\Python_algorithm\\game\\file\\ND2.csv", index=False)
