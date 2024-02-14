import numpy as np
import pandas as pd

df = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\base.csv")

groups = df.groupby(['set_no', 'game_no'])
data = []
for index, group in groups:
    group.reset_index(drop=True, inplace=True)
    # p1得分 p2得分
    p1_get_point = len(group[group['point_victor'] == 1])
    p2_get_point = len(group[group['point_victor'] == 2])
    # 总分
    all_point = group['point_no'].max() - group['point_no'].min() + 1
    # 发球数
    serve_num = len(group[group['server'] == 1])

    # serve
    serve = serve_num / all_point
    # p1_points_won, p2_points_won
    p1_points_won, p2_points_won = np.asarray([p1_get_point, p2_get_point]) / all_point
    # p1_ace, p2_ace
    p1_ace = (group[['p1_ace']].sum() / serve_num).fillna(0).values[0]
    p2_ace = (group[['p2_ace']].sum() / (all_point - serve_num)).fillna(0).values[0]
    # p1_winner, p2_winner
    p1_winner, p2_winner = (group[['p1_winner', 'p2_winner']].sum()) / all_point
    # p1_double_fault, p2_double_fault
    p1_double_fault = (group[['p1_double_fault']].sum() / serve_num).fillna(0).values[0]
    p2_double_fault = (group[['p2_double_fault']].sum() / (all_point - serve_num)).fillna(0).values[0]

    # p1_unf_err, p2_unf_err
    p1_unf_err = (group[['p1_unf_err']].sum() / p2_get_point).fillna(0).values[0]
    p2_unf_err = (group[['p2_unf_err']].sum() / p1_get_point).fillna(0).values[0]
    # p1_net_pt, p2_net_pt
    p1_net_pt, p2_net_pt = (group[['p1_net_pt_won', 'p2_net_pt_won']].sum().reset_index(drop=True) / group[
        ['p1_net_pt', 'p2_net_pt']].sum().reset_index(drop=True)).fillna(0)

    # p1_break_pt, p2_break_pt
    p1_break_pt, p2_break_pt = (group[['p1_break_pt_won', 'p2_break_pt_won']].sum().reset_index(drop=True) / group[
        ['p1_break_pt', 'p2_break_pt']].sum().reset_index(drop=True)).fillna(0)
    # p1_distance_run, p2_distance_run
    temp = group.iloc[:, list(range(38, 40))]
    p1_distance_run, p2_distance_run = temp['p1_distance_run'].mean(), temp['p2_distance_run'].mean()
    # speed_mph
    speed_mph, serve_width, serve_depth, return_depth = group[
        ['speed_mph', 'serve_width', 'serve_depth', 'return_depth']].max()
    data.append(
        [serve, p1_points_won, p2_points_won, p1_ace, p2_ace, p1_winner, p2_winner, p1_double_fault, p2_double_fault,
         p1_unf_err, p2_unf_err, p1_net_pt, p2_net_pt, p1_break_pt, p2_break_pt, p1_distance_run, p2_distance_run,
         speed_mph, serve_width, serve_depth, return_depth])
pd.DataFrame(data, columns=['serve', 'p1_points_won', 'p2_points_won', 'p1_ace', 'p2_ace', 'p1_winner', 'p2_winner',
                            'p1_double_fault', 'p2_double_fault', 'p1_unf_err', 'p2_unf_err', 'p1_net_pt', 'p2_net_pt',
                            'p1_break_pt', 'p2_break_pt', 'p1_distance_run', 'p2_distance_run', 'speed_mph',
                            'serve_width', 'serve_depth', 'return_depth']) \
    .to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\fucking.csv", index=False)
