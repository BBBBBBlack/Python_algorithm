# 平均表现得分
import pandas as pd
from datetime import datetime


def sum_by_games(data):
    return data['1'].mean()


# 表现斜率

time_start_col = []
perform_mean_col = []
t = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC2.csv")
t = t[['elapsed_time', 'set_no', 'game_no', '1']]
groups = t.groupby(['set_no', 'game_no'])
for index, group in groups:
    group.reset_index(drop=True, inplace=True)
    time_start_col.append(group['elapsed_time'][0])
    perform_mean_col.append(sum_by_games(group))
AC_p2_1 = pd.concat([pd.DataFrame(time_start_col), pd.DataFrame(perform_mean_col)], axis=1, ignore_index=True)
# AC_p2_1 = pd.DataFrame(time_start_col, perform_mean_col)
AC_p2_1.to_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_p2_perform_mean.csv", index=False)
