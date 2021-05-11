# from array import array
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import find_peaks
#
#
# def acf(xx, length=20):
#     return np.array([1] + [np.corrcoef(xx[:-ii], xx[ii:], )[0, 1] for ii in range(1, length)])
#
#
# def autocorr(xx, t=1):
#     return np.corrcoef(np.array([xx[:-t], xx[t:]]))
#
#
# def column(matrix, ii):
#     return [row[ii] for row in matrix]
#
#
# with open('DATA/folderB/dataB.dat', 'rb') as file:
#     float_array = array('f')
#     float_array.fromstring(file.read())
#
# # aaa = np.reshape(float_array, (-1, 5))
# # a = column(aaa, 1)
# # print(a)
#
#
# def aaa(start, end_arg):
#     count = 0
#
#     end = end_arg
#
#     for i in range(start, end):
#         for j in range(i, end):
#             yy = y[i:j]
#             a = acf(yy, len(yy))
#             maximums = find_peaks(a)
#             count += 1
#             print(f'\r{count}', end="")
#         # print(a)
#
#             if len(maximums[0]) != 0 and a[maximums[0][0]] >= 0.999:
#                 plt.scatter([maximums[0][0]], [a[maximums[0][0]]])
#                 plt.plot(a)
#                 plt.show()
#                 return True
#
#
# step = .01
# x = np.arange(0, 13, step)
# y = np.sin(x)
# plt.plot(x, y)
# aaa(600, len(x) - 1)
#
# # aa = autocorr(yy, 1998)
# #
# # plt.plot(aa)
# # print(aa)
# # plt.show()
#
# # for shit in range(10):
# #     correlation = np.corrcoef(y[:shit],
# #                               y[shit:])[0, 1]
# #     autocorrelation.append(correlation)
#
# # plt.plot(autocorrelation)
# # plt.show()


import govnocode


while True:
    lst = []
    boolean1 = False
    boolean2 = False

    for i in range(4):
        boolean1, value1 = govnocode.run_algorithm('DATA/folderF/dataF.dat', i + 1)

    for i in range(4):
        boolean2, value2 = govnocode.run_algorithm('DATA/folderB/dataB.dat', i + 1)

    lst.append(boolean1)
    lst.append(boolean2)

    if not lst.__contains__(False):
        break

print("Stop!!!!!!")
