# 分为p1_serve, p1_return, p2_serve, p2_return四个文件
import pandas as pd


def process_serve(serve):
    serve.drop(['return_depth', 'server', 'break_pt', 'break_pt_won', 'break_pt_missed', 'winner'], axis=1,
               inplace=True)
    serve['double_fault'] = serve['double_fault'].map({'1': -1, 1: -1, '0': 0, 0: 0})
    serve['unf_err'] = serve['unf_err'].map({'1': -1, 1: -1, '0': 0, 0: 0})
    return serve


def process_return(return_):
    return_.drop(['speed_mph', 'serve_width', 'serve_depth', 'server', 'double_fault', 'ace'], axis=1,
                 inplace=True)
    return_['unf_err'] = return_['unf_err'].map({'1': -1, 1: -1, '0': 0, 0: 0})
    return_.loc[return_['break_pt_won'] == 1, 'break_pt'] = -1
    return_.loc[return_['break_pt_missed'] == 1, 'break_pt'] = 1
    return_.drop(['break_pt_won', 'break_pt_missed'], axis=1, inplace=True)
    return return_


df = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\base.csv")

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
AC_serve = process_serve(AC_serve)
AC_return = AC[AC['server'] == 2]
AC_return = process_return(AC_return)

# 对ND执行同样的操作
DM = pd.concat([df['elapsed_time'], df['server'], df['p2_ace'], df['p2_winner'], df['p2_double_fault'],
                df['p2_unf_err'], df['p2_net_pt_won'], df['p2_break_pt'],
                df['p2_break_pt_won'], df['p2_break_pt_missed'], df['p2_distance_run'],
                df['speed_mph'], df['serve_width'], df['serve_depth'], df['return_depth'], df['point_victor']], axis=1)
DM.columns = columns
DM['point_victor'] = DM['point_victor'].map({1: 0, 2: 1, '1': 0, '2': 1})

DM_serve = DM[DM['server'] == 2]
DM_serve = process_serve(DM_serve)
DM_return = DM[DM['server'] == 1]
DM_return = process_return(DM_return)
# save
AC_serve.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_serve.csv", index=False)
AC_return.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_return.csv", index=False)
DM_serve.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_serve.csv", index=False)
DM_return.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_return.csv", index=False)
