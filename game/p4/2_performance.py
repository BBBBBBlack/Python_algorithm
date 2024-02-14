# 计算表现评分
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import pandas as pd

RIS = (None, 0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59)


# 判断一致性
def judge_consist(array):
    val, ten = np.linalg.eig(array)
    # 最大特征值
    lam_max = np.max(val)
    CI = (lam_max - array.shape[0]) / (array.shape[0] - 1)
    RI = RIS[array.shape[0]]
    CR = CI / RI
    if CR < 0.1:
        print("一致性检验通过")
        return True
    else:
        print("一致性检验不通过")
        return False


# 特征值法
def weight_feature(array):
    lam, ten = np.linalg.eig(array)
    lam_idx_max = np.argmax(lam)
    # 最大特征值对应的特征向量!!!
    ten_max = ten[:, lam_idx_max].real
    # 归一化
    return ten_max / ten_max.sum()


# 变异系数法
def weight_cv(array):
    # 变异系数
    # 标准化
    array /= np.sqrt(np.sum(np.power(array, 2), axis=1))
    cv = np.std(array, axis=1) / np.mean(array, axis=1)
    return cv / cv.sum()


def weight(array):
    w1 = weight_cv(array)
    w2 = weight_feature(array)
    return np.sqrt(np.power(w1 * w2, 2) / np.power(w1 * w2, 2).sum())


# 算权重
def cal_weight(arr_data, arr_weight):
    return np.dot(arr_data, arr_weight)


def change_time(df):
    df['elapsed_time'] = pd.to_datetime(df['elapsed_time'], format='%H:%M:%S')
    return df


# 归一化
def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


def merge(serve, return_, serve_weight, return_weight):
    serve_real = serve.iloc[:, 1:].to_numpy()
    serve_time = serve.iloc[:, 0].to_numpy()
    serve_score = cal_weight(serve_real, serve_weight)
    # 对数据进行归一化处理
    serve_score = normalize(serve_score)
    s = pd.concat([pd.DataFrame(serve_time), pd.DataFrame(serve_score)], axis=1, ignore_index=True)
    return_real = return_.iloc[:, 1:].to_numpy()
    return_time = return_.iloc[:, 0].to_numpy()
    return_score = cal_weight(return_real, return_weight)
    # 对数据进行归一化处理
    return_score = normalize(return_score)
    r = pd.concat([pd.DataFrame(return_time), pd.DataFrame(return_score)], axis=1, ignore_index=True)
    return pd.concat([s, r]).sort_values(0)


AC_serve = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_serve.csv")
AC_return = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_return.csv")
ND_serve = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_serve.csv")
ND_return = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_return.csv")
AC_serve = change_time(AC_serve)
AC_return = change_time(AC_return)
ND_serve = change_time(ND_serve)
ND_return = change_time(ND_return)

# 一致性检验——serve
arr_serve = np.asarray([
    [1, 2, 2, 2, 2, 2, 2, 2, 4],
    [1 / 2, 1, 1, 1, 1, 2, 2, 2, 3],
    [1 / 2, 1, 1, 1, 1, 2, 2, 2, 3],
    [1 / 2, 1, 1, 1, 1, 2, 2, 2, 3],
    [1 / 2, 1, 1, 1, 1, 2, 2, 2, 3],
    [1 / 2, 1 / 2, 1 / 2, 1 / 2, 2, 1, 1, 1, 2],
    [1 / 2, 1 / 2, 1 / 2, 1 / 2, 2, 1, 1, 1, 2],
    [1 / 2, 1 / 2, 1 / 2, 1 / 2, 1 / 2, 1, 1, 1, 2],
    [1 / 4, 1 / 3, 1 / 3, 1 / 3, 1 / 3, 1 / 2, 1 / 2, 1 / 2, 1]
])
arr_return = np.asarray([
    [1, 3, 3, 5, 3, 3, 2],
    [1 / 3, 1, 1, 3, 1, 1, 1],
    [1 / 3, 1, 1, 3, 1, 1, 1],
    [1 / 5, 1 / 3, 1 / 3, 1, 1 / 3, 1 / 3, 1 / 3],
    [1 / 3, 1, 1, 3, 1, 1, 1],
    [1 / 3, 1, 1, 3, 1, 1, 1],
    [1 / 2, 1, 1, 3, 1, 1, 1]
])
if judge_consist(arr_serve) & judge_consist(arr_return):
    serve_weight = weight(arr_serve)
    # serve_weight = np.asarray(serve_weight)
    # serve_weight/=serve_weight.sum()
    return_weight = weight(arr_return)
    # return_weight = np.asarray(return_weight)
    # return_weight/=return_weight.sum()
    print("serve_weight:", serve_weight)
    print("return_weight:", return_weight)

    AC_res = merge(AC_serve, AC_return, serve_weight, return_weight)

    # 画图
    plt.figure(figsize=(16, 10))
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2)  # 设置x轴粗细为2
    ax.spines['left'].set_linewidth(2)  # 设置y轴粗细为2
    plt.tick_params(axis='x', labelsize=15)  # 设置x轴标号的字体大小为12
    plt.tick_params(axis='y', labelsize=18)  # 设置y轴标号的字体大小为12
    plt.plot(AC_res[0], AC_res[1], label='Carlos Alcaraz\'s performance score',
             color='#f3515f', linewidth=2)
    plt.xticks(rotation=45)
    ND_res = merge(ND_serve, ND_return, serve_weight, return_weight)
    plt.plot(ND_res[0], ND_res[1], label='Nicolas Jarry\'s performance score',
             linewidth=2)
    plt.xticks(rotation=45)
    plt.xlabel('time', fontsize=20)
    plt.ylabel('performance score', fontsize=20)
    plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
    plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=3))
    plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 01:49:13'))
    plt.legend(prop={'size': 20})

    # 局部放大
    # 创建一个嵌套的坐标系并设置位置和大小
    ax_ins = inset_axes(ax, width="40%", height="30%", loc='upper right',
                        bbox_to_anchor=(0.1, 0.1, 1, 1),
                        bbox_transform=ax.transAxes)  # 在嵌套的坐标系中绘制局部放大的部分
    ax_ins.set_xlim(0, 1)
    ax_ins.set_ylim(0, 1)
    base = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\base.csv")

    # length = len(g)[0]
    # ax_ins.plot(AC_res[0], AC_res[1])
    # ax_ins.plot(ND_res[0], ND_res[1])

    AC_res.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_perform.csv", index=False)
    ND_res.to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_perform.csv", index=False)

# 画图
plt.figure(figsize=(12, 6))
AC_games = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_games.csv")
DM_games = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_games.csv")
plt.xlabel('game_no')
plt.ylabel('performance score')
plt.plot(range(1, len(AC_games) + 1), AC_games['is_win'].to_numpy(), label='actual result',
         linewidth=2)
plt.plot(range(1, len(AC_games) + 1), AC_games['mean_performance'].to_numpy(),
         color='#f3515f', label='Carlos Alcaraz\'s performance score', linewidth=2)

plt.legend()
plt.show()
