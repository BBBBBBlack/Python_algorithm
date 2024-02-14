# p1以局为单位计算表现斜率
import pandas as pd
from datetime import datetime


def sum_by_games(data):
    data.reset_index(drop=True, inplace=True)
    date1 = datetime.strptime(data['elapsed_time'][len(data) - 1], '%Y-%m-%d %H:%M:%S')
    date2 = datetime.strptime(data['elapsed_time'][0], '%Y-%m-%d %H:%M:%S')
    return (data['1'][len(data) - 1] - data['1'][0]) / (date1 - date2).seconds


# 表现斜率
new_col = []
t = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC2.csv")
t = t[['elapsed_time', 'set_no', 'game_no', '1']]
groups = t.groupby(['set_no', 'game_no'])
for index, group in groups:
    new_col.append(sum_by_games(group))
AC_p2_1 = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_p2_1.csv")
AC_p2_1['performance'] = new_col
AC_p2_1['con_pro_lose'] *= -1
AC_p2_1['con_game_lose'] *= -1
AC_p2_1['con_set_lose'] *= -1
AC_p2_1.to_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_p2_1.csv", index=False)
