import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
# Novak Djokovic的平均发球速度
DN_avg_speed = df['speed_mph'][df['server'] == 2].dropna().sum() / df['speed_mph'][df['server'] == 2].dropna().count()
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 1), 'speed_mph'] = AC_avg_speed
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 2), 'speed_mph'] = DN_avg_speed

# AC = df[(df['player1'] == 'Carlos Alcaraz') | (df['player2'] == 'Carlos Alcaraz')]

# 分离p1和p2的数据
columns = ['elapsed_time', 'server', 'ace', 'winner',
           'double_fault', 'unf_err', 'net_pt_won',
           'break_pt', 'break_pt_won', 'break_pt_missed', 'distance_run',
           'speed_mph', 'serve_width', 'serve_depth', 'return_depth', 'point_victor']
AC = pd.concat([df['elapsed_time'], df['server'], df['p1_ace'], df['p1_winner'], df['p1_double_fault'],
                df['p1_unf_err'], df['p1_net_pt_won'], df['p1_break_pt'],
                df['p1_break_pt_won'], df['p1_break_pt_missed'], df['p1_distance_run'],
                df['speed_mph'], df['serve_width'], df['serve_depth'], df['return_depth'], df['point_victor']], axis=1)

AC.columns = columns
AC['point_victor'] = AC['point_victor'].map({1: 1, 2: 0, '1': 1, '2': 0})

AC_serve = AC[AC['server'] == 1]
AC_serve.drop(['return_depth', 'server', 'break_pt', 'break_pt_won', 'break_pt_missed', 'winner'], axis=1, inplace=True)
AC_return = AC[AC['server'] == 2]
AC_return.drop(['speed_mph', 'serve_width', 'serve_depth', 'server', 'double_fault', 'ace'], axis=1,
               inplace=True)

# 对ND执行同样的操作
ND = pd.concat([df['elapsed_time'], df['server'], df['p2_ace'], df['p2_winner'], df['p2_double_fault'],
                df['p2_unf_err'], df['p2_net_pt_won'], df['p2_break_pt'],
                df['p2_break_pt_won'], df['p2_break_pt_missed'], df['p2_distance_run'],
                df['speed_mph'], df['serve_width'], df['serve_depth'], df['return_depth'], df['point_victor']], axis=1)
ND.columns = columns
ND['point_victor'] = ND['point_victor'].map({1: 0, 2: 1, '1': 0, '2': 1})

ND_serve = ND[ND['server'] == 2]
ND_serve.drop(['return_depth', 'server', 'break_pt', 'break_pt_won', 'break_pt_missed', 'winner'], axis=1, inplace=True)
ND_return = ND[ND['server'] == 1]
ND_return.drop(['speed_mph', 'serve_width', 'serve_depth', 'server', 'double_fault', 'ace'], axis=1,
               inplace=True)

total_serve = pd.concat([AC_serve, ND_serve], axis=0)
total_serve['double_fault'] = total_serve['double_fault'].map({'1': -1, 1: -1, '0': 0, 0: 0})
total_serve['unf_err'] = total_serve['unf_err'].map({'1': -1, 1: -1, '0': 0, 0: 0})
total_return = pd.concat([AC_return, ND_return], axis=0)
total_return['unf_err'] = total_return['unf_err'].map({'1': -1, 1: -1, '0': 0, 0: 0})
total_return.loc[total_return['break_pt_won'] == 1, 'break_pt'] = -1
total_return.loc[total_return['break_pt_missed'] == 1, 'break_pt'] = 1
total_return.drop(['break_pt_won', 'break_pt_missed'], axis=1, inplace=True)

total_serve.to_csv("C:\\Users\\black\Downloads\\total_serve.csv", index=False)
total_return.to_csv("C:\\Users\\black\Downloads\\total_return.csv", index=False)

total_serve.drop('elapsed_time', axis=1, inplace=True)
total_return.drop('elapsed_time', axis=1, inplace=True)

# 绘制热力图
plt.figure(figsize=(10, 8))
spearman_corr = total_serve.corr(method='spearman')
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('AC Spearman Correlation Heatmap')
plt.figure(figsize=(10, 8))
spearman_corr = total_return.corr(method='spearman')
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('DN Spearman Correlation Heatmap')
plt.show()
