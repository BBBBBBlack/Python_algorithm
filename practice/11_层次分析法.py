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


# 权重——算术平均法
def weight_avg(array):
    # 归一化
    col_sum = array.sum(axis=0)
    array = array / col_sum
    # 按行求和
    row_sum = array.sum(axis=1)
    return row_sum / array.shape[0]


# 权重——几何平均法
def weight_geometry(array):
    row_cum = array.prod(axis=1)
    row_cum = np.power(row_cum, 1 / array.shape[0])
    return row_cum / row_cum.sum()


# 特征值法
def weight_feature(array):
    lam, ten = np.linalg.eig(array)
    lam_idx_max = np.argmax(lam)
    # 最大特征值对应的特征向量!!!
    ten_max = ten[:, lam_idx_max].real
    # 归一化
    return ten_max / ten_max.sum()


# 构造判断矩阵
# 选择旅游地
sel = np.asarray([[1, 1 / 2, 4, 3, 3],
                  [2, 1, 7, 5, 5],
                  [1 / 4, 1 / 7, 1, 1 / 2, 1 / 3],
                  [1 / 3, 1 / 5, 2, 1, 1],
                  [1 / 3, 1 / 5, 3, 1, 1]])
# 景色
since = np.asarray([[1, 2, 5],
                    [1 / 2, 1, 2],
                    [1 / 5, 1 / 2, 1]])
# 花费
fee = np.asarray([[1, 1 / 3, 1 / 8],
                  [3, 1, 1 / 3],
                  [8, 3, 1]])
# 居住
live = np.asarray([[1, 1, 3],
                   [1, 1, 3],
                   [1 / 3, 1 / 3, 1]])
# 饮食
food = np.asarray([[1, 3, 4],
                   [1 / 3, 1, 1],
                   [1 / 4, 1, 1]])
# 交通
traffic = np.asarray([[1, 1, 1 / 4],
                      [1, 1, 1 / 4],
                      [4, 4, 1]])
# traffic = np.array([[1, 4, 1 / 2], [1 / 4, 1, 1 / 4], [2, 4, 1]])
# 一致性检验
ele = np.asarray([since, fee, live, food, traffic])
if judge_consist(sel):
    for i in ele:
        if not judge_consist(i):
            break
    # 计算权重
    sel = weight_feature(sel)
    weight_list = []
    for i in ele:
        weight_list.append(weight_feature(i))
    df = pd.DataFrame(weight_list, index=["准则" + str(i) for i in range(sel.shape[0])],
                      columns=["方案" + str(i) for i in range(since.shape[0])])
    weight_list = np.asarray(weight_list)
    print(np.dot(sel.reshape(1, 5), weight_list))
    print(df)
