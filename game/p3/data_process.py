import matplotlib.pyplot as plt
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
# Novak Djokovic的平均发球速度
DN_avg_speed = df['speed_mph'][df['server'] == 2].dropna().sum() / df['speed_mph'][df['server'] == 2].dropna().count()
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 1), 'speed_mph'] = AC_avg_speed
df.loc[(df['speed_mph'].isnull()) & (df['server'] == 2), 'speed_mph'] = DN_avg_speed
groups = df.groupby(['set_no', 'game_no'])
data = []
for index, group in groups:
    group.reset_index(drop=True, inplace=True)
    # p1 p2得分比
    scores = len(group[group['point_victor'] == 1]) - len(group[group['point_victor'] == 2])
    temp = len(group[group['server'] == 1]) - len(group[group['server'] == 2])
    # 发球数
    serve = 0
    if temp == 0:
        # 发球数各自相同
        serve = 0
    elif temp > 0:
        # p1发球数多
        serve = 1
    else:
        # p2发球数多
        serve = 2
    p1_points_won, p2_points_won = group[['p1_points_won', 'p2_points_won']].max().to_list()
    p1_ace, p2_ace, p1_winner, p2_winner, p1_double_fault, \
        p2_double_fault, p1_unf_err, p2_unf_err, p1_net_pt, \
        p2_net_pt, p1_net_pt_won, p2_net_pt_won, p1_break_pt, \
        p2_break_pt, p1_break_pt_won, p2_break_pt_won, \
        p1_break_pt_missed, p2_break_pt_missed, rally_count \
        = group.iloc[:, list(range(20, 24)) + list(range(24, 38)) + list(range(40, 41))].sum()
    p1_distance_run, p2_distance_run, speed_mph, serve_width, \
        serve_depth, return_depth \
        = group.iloc[:, list(range(38, 40)) + list(range(41, 45))].mean()
    data.append([scores, serve, p1_points_won, p2_points_won, p1_ace, p2_ace, p1_winner, p2_winner, p1_double_fault,
                 p2_double_fault, p1_unf_err, p2_unf_err, p1_net_pt, p2_net_pt, p1_net_pt_won, p2_net_pt_won,
                 p1_break_pt, p2_break_pt, p1_break_pt_won, p2_break_pt_won, p1_break_pt_missed, p2_break_pt_missed,
                 rally_count, p1_distance_run, p2_distance_run, speed_mph, serve_width, serve_depth, return_depth])
pd.DataFrame(data, columns=['scores', 'serve', 'p1_points_won', 'p2_points_won', 'p1_ace', 'p2_ace', 'p1_winner',
                            'p2_winner', 'p1_double_fault', 'p2_double_fault', 'p1_unf_err', 'p2_unf_err', 'p1_net_pt',
                            'p2_net_pt', 'p1_net_pt_won', 'p2_net_pt_won', 'p1_break_pt', 'p2_break_pt',
                            'p1_break_pt_won',
                            'p2_break_pt_won', 'p1_break_pt_missed', 'p2_break_pt_missed', 'rally_count',
                            'p1_distance_run',
                            'p2_distance_run', 'speed_mph', 'serve_width', 'serve_depth', 'return_depth']) \
    .to_csv("D:\\xxx\\Python_algorithm\\game\\file\\file\\Wimbledon_featured_matches.csv", index=False)
