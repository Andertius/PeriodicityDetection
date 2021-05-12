from time import sleep
import math


index = 0
index1 = 0.0
index2 = 0.0
index3 = 0.0
index4 = 0.0
index5 = 0.0
index6 = 0.0
index7 = 0.0
index8 = 0.0

while True:
    data = [index,
            math.sin(index1),
            math.sin(index2 * math.pi / 2),
            math.cos(2 * index3),
            math.cos(math.sin(index4))]
    s = ""

    for i in range(len(data)):
        s += f"{data[i]} "

    s += "\n"
    f = open('DATA/folderB/dataB.dat', 'a')
    f.write(s)
    f.close()

    data = [index,
            math.sin(math.cos(index5)),
            math.pow(math.sin(index6), 2) / 5 + math.cos(index6 / 2) * math.sin(index6),
            math.pow(math.sin(index7), 2) * math.cos(index7),
            math.sin(index8 + math.pi / 4) + math.cos(index8 + math.pi / 4)]
    s = ""

    for i in range(len(data)):
        s += f"{data[i]} "

    s += "\n"
    f = open('DATA/folderF/dataF.dat', 'a')
    f.write(s)
    f.close()

    index += 1
    index1 += 0.1
    index2 += 0.1
    index3 += 0.1
    index4 += 0.1
    index5 += 0.1
    index6 += 0.1
    index7 += 0.1
    index8 += 0.1

    if index1 >= math.pi * 2:
        index1 = 0

    if index2 >= 4:
        index2 = 0

    if index3 >= math.pi:
        index3 = 0

    if index4 >= math.pi:
        index4 = 0

    if index5 >= math.pi * 2:
        index5 = 0

    if index6 >= math.pi * 4:
        index6 = 0

    if index7 >= math.pi * 2:
        index7 = 0

    if index8 >= math.pi * 2:
        index8 = 0

    sleep(0.5)
