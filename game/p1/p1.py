import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RIS = (None, 0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59)
alpha = 0.5
beta = 0.5


# 判断一致性
def judge_consist(array):
    val, ten = np.linalg.eig(array)
    # 最大特征值
    lam_max = np.max(val)
    CI = (lam_max - array.shape[0]) / (array.shape[0] - 1)
    RI = RIS[array.shape[0]]
    CR = CI / RI
    print("CR:", CR)
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


def weight(array, alpha, beta):
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


AC_serve = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_serve.csv")
AC_return = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_return.csv")
ND_serve = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\ND_serve.csv")
ND_return = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\ND_return.csv")
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
    judge_consist(arr_serve)
    judge_consist(arr_return)
    plt.figure(figsize=(30, 12))
    serve_weight = weight(arr_serve, alpha, beta)
    return_weight = weight(arr_return, alpha, beta)
    print(serve_weight)
    print(return_weight)

    AC_res = merge(AC_serve, AC_return, serve_weight, return_weight)

    plt.plot(AC_res[0], AC_res[1], label='Carlos Alcaraz')
    plt.xticks(rotation=45)

    plt.gcf().autofmt_xdate()
    ND_res = merge(ND_serve, ND_return, serve_weight, return_weight)
    plt.plot(ND_res[0], ND_res[1], label='Nicolas Jarry', color='red')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
    plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=15))
    plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 04:45:00'))
    plt.legend(prop={'size': 20})
    plt.show()
    AC_res.to_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_perform.csv", index=False)
    ND_res.to_csv("D:\\xxx\\Python_algorithm\\game\\file\\ND_perform.csv", index=False)
