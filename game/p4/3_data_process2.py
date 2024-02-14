# 以局为单位分离的准备，分离p1，p2，加上perform
import pandas as pd


def change(data):
    data['elapsed_time'] = pd.to_datetime(data['elapsed_time'], format='%H:%M:%S')
    data.reset_index(drop=True, inplace=True)
    return data


df = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\base.csv")

# 分离p1和p2的数据
columns = ['elapsed_time', 'set_no', 'game_no', 'point_no', 'sets', 'games', 'server', 'point_victor']
AC2 = pd.concat(
    [df['elapsed_time'], df['set_no'], df['game_no'], df['point_no'],
     df['p1_sets'], df['p1_games'], df['server'], df['point_victor']], axis=1)
AC2.columns = columns

# 对ND执行同样的操作
DM2 = pd.concat(
    [df['elapsed_time'], df['set_no'], df['game_no'], df['point_no'],
     df['p2_sets'], df['p2_games'], df['server'], df['point_victor']], axis=1)
DM2.columns = columns

AC2.loc[AC2['server'] == 2, 'server'] = 0
AC2['point_victor'] = AC2['point_victor'].map({1: 1, 2: 0})
DM2.loc[DM2['server'] == 1, 'server'] = 0
DM2.loc[DM2['server'] == 2, 'server'] = 1
DM2['point_victor'] = DM2['point_victor'].map({1: 0, 2: 1})

AC2 = change(AC2)
DM2 = change(DM2)

tt = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_perform.csv")
AC2 = pd.concat([AC2, tt['1']], axis=1)
tt = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_perform.csv")
DM2 = pd.concat([DM2, tt['1']], axis=1)
# save
AC2.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_games_perform.csv", index=False)
DM2.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_games_perform.csv", index=False)
