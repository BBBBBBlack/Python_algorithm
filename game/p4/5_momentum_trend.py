# 计算动量、走势（平均表现得分差）
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as dates
import pandas as pd


# 标准化
def standardization(array):
    array = array.to_numpy()
    return (array - array.min()) / (array.max() - array.min())


# 变异系数法
def weight_cv(array):
    # 变异系数
    cv = np.std(array, axis=0) / np.mean(array, axis=0)
    return cv / cv.sum()


AC_games = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_games.csv")
DM_games = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_games.csv")
# 标准化
AC = AC_games.drop(['elapsed_time', 'mean_performance', 'is_win'], axis=1)
DM = DM_games.drop(['elapsed_time', 'mean_performance', 'is_win'], axis=1)
AC = standardization(AC)
DM = standardization(DM)
AC_weight = weight_cv(AC)
DM_weight = weight_cv(DM)
print(AC_weight)
print(DM_weight)
# 变异系数
AC_val = np.dot(AC, AC_weight)
DM_val = np.dot(DM, DM_weight)
AC_perform = AC_games['mean_performance']
DM_perform = DM_games['mean_performance']
AC_time = pd.to_datetime(AC_games['elapsed_time'])
DM_time = pd.to_datetime(DM_games['elapsed_time'])

plt.figure(figsize=(8, 6), dpi=300)
plt.gca().set_aspect(0.35)
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=20))
plt.xticks(rotation=45)
plt.xlabel('time')
plt.ylabel('momentum')
plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 04:45:00'))
plt.ylim(0.18, 0.52)
# plt.title('Two players\' momentum')
plt.plot(AC_time.to_numpy()[1:], AC_val[1:], color='#f3515f', label='Carlos Alcaraz\'s momentum')
plt.plot(DM_time.to_numpy()[1:], DM_val[1:], label='Novak Djokovic\'s momentum')
plt.legend(loc='upper left')

plt.figure(figsize=(8, 6), dpi=300)
plt.gca().set_aspect(0.03)
# plt.title('Carlos Alcaraz\'s momentum and mean performance')
plt.plot(AC_time.to_numpy()[1:], AC_val[1:], color='#f3515f', label='Carlos Alcaraz\'s momentum')
plt.plot(AC_time.to_numpy()[1:], AC_perform.to_numpy()[1:], label='Carlos Alcaraz\'s performance score')
plt.plot(AC_time.to_numpy()[1:], AC_games['con_pro_win'].to_numpy()[1:], color='#fdb933',
         label='Carlos Alcaraz\'s cumulative score')
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=20))
plt.xticks(rotation=45)
plt.xlabel('time')
plt.ylabel('outcome')
plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 04:45:00'))
plt.ylim(0, 4.5)
plt.legend(loc='upper left')

plt.figure(figsize=(8, 6), dpi=300)
plt.gca().set_aspect(0.03)
# plt.title('Novak Djokovic\'s momentum and mean performance')
plt.plot(DM_time.to_numpy()[1:], DM_val[1:], label='Novak Djokovic\'s momentum')
plt.plot(DM_time.to_numpy()[1:], DM_perform.to_numpy()[1:], label='Novak Djokovic\'s performance score')
plt.plot(DM_time.to_numpy()[1:], DM_games['con_pro_win'].to_numpy()[1:], color='#fdb933',
         label='Novak Djokovic\'s cumulative score')
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=20))
plt.xticks(rotation=45)
plt.xlabel('time')
plt.ylabel('outcome')
plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 04:45:00'))
plt.ylim(0, 4.5)
plt.legend(loc='upper left')

plt.figure(figsize=(10, 8), dpi=300)
plt.gca().set_aspect(0.2)
# plt.title('Carlos Alcaraz\'s momentum and mean performance difference')
plt.plot(AC_time.to_numpy()[1:], AC_val[1:], color='#f3515f', label='Carlos Alcaraz\'s momentum')
plt.plot(AC_time.to_numpy()[1:], (AC_perform.to_numpy() - DM_perform.to_numpy())[1:],
         label='performance score difference')
plt.xlabel('time')
plt.ylabel('outcome')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=20))
plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 04:45:00'))
plt.ylim(-0.2, 0.5)
plt.legend(loc='upper left')

plt.figure(figsize=(10, 8), dpi=300)
plt.gca().set_aspect(0.2)
# plt.title('Novak Djokovic\'s momentum and mean performance difference')
plt.plot(DM_time.to_numpy()[1:], DM_val[1:], color='#f3515f', label='Novak Djokovic\'s momentum')
plt.plot(DM_time.to_numpy()[1:], (DM_perform.to_numpy() - AC_perform.to_numpy())[1:],
         label='performance score difference')
plt.xlabel('time')
plt.ylabel('outcome')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(dates.MinuteLocator(interval=20))
plt.xlim(pd.to_datetime('1900-01-01 00:00:00'), pd.to_datetime('1900-01-01 04:45:00'))
plt.ylim(-0.2, 0.5)
plt.legend(loc='upper left')
plt.show()

pd.concat(
    [pd.DataFrame(AC_val, columns=['momentum']), AC_perform - DM_perform,
     AC_games['con_pro_win']],
    axis=1).to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_momentum_trend.csv", index=False)

pd.concat(
    [pd.DataFrame(DM_val, columns=['momentum']), DM_perform - AC_perform,
     AC_games['con_pro_win']],
    axis=1).to_csv("D:\\xxx\\Python_algorithm\\game\\file2\\DM_momentum_trend.csv", index=False)
