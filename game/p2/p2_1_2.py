# 处理p2的数据，转换为games为单位
import pandas as pd


def cal_consecutive(arr):
    f_win = 0
    f_loss = 0
    con_win = 0
    con_lose = 0
    # 是否连续
    flag_win = 0
    flag_loss = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            flag_loss = 0
            if flag_win == 0:
                con_win = 1
                flag_win = 1
            else:
                con_win += 1
        else:
            flag_win = 0
            if flag_loss == 0:
                con_lose = 1
                flag_loss = 1
            else:
                con_lose += 1
        f_win = max(f_win, con_win)
        f_loss = max(f_loss, con_lose)
    return f_win, f_loss


def cal_total_game(s_win, g_win, p_win):
    temp = p2_dataset()
    temp.con_pro_win, temp.con_pro_lose = cal_consecutive(p_win)
    temp.con_game_win, temp.con_game_lose = cal_consecutive(g_win)
    temp.con_set_win, temp.con_set_lose = cal_consecutive(s_win)
    return temp


class p2_dataset():
    def __init__(self):
        self.con_pro_win = 0
        self.con_pro_lose = 0
        self.con_game_win = 0
        self.con_game_lose = 0
        self.con_set_win = 0
        self.con_set_lose = 0
        self.is_server = 0


ND2 = pd.read_csv('D:\\xxx\\Python_algorithm\\game\\file\\ND2.csv')
# 按games划分
groups = ND2.groupby('set_no')
objects = []
s_win = []
for index_s, set_ in groups:
    games = set_.groupby('game_no')
    g_win = []
    for index_g, game in games:
        if len(game[game['point_victor'] == 1]) > len(game[game['point_victor'] == 0]):
            g_win.append(1)
        else:
            g_win.append(0)
        if index_g == len(games):

            if sum(x == 1 for x in g_win) > sum(x == 0 for x in g_win):
                s_win.append(1)
            else:
                s_win.append(0)
        object = cal_total_game(s_win, g_win, game['point_victor'].to_list())
        if len(game[game['server'] == 1]) > len(game[game['server'] == 0]):
            object.is_server = 1
        elif len(game[game['server'] == 1]) < len(game[game['server'] == 0]):
            object.is_server = -1
        else:
            object.is_server = 0
        objects.append(object)
AC_p2_1 = pd.DataFrame([vars(obj) for obj in objects])
AC_p2_1.to_csv('D:\\xxx\\Python_algorithm\\game\\file\\ND_p2_1.csv', index=False)
