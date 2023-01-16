from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve

#Zavd 1 function
def zavd1(num):
    p = num * (lens + 1) - 1
    ans = rating[int(p)] + (p % int(p)) * (rating[int(p) + 1] - rating[int(p)])
    return ans
#Zavd 2 function
def zavd2():
    suma = 0
    total = 0
    totalSum = 0
    for i in range(lens):
        suma += rating[i]

    for i in range(lens):
        total += (rating[i] - (suma / lens)) ** 2
        totalSum += abs(rating[i] - (suma / lens))

    result = total / lens
    Result = totalSum / lens
    print("Стандартне відхилення = ", str(round(sqrt(result))))
    print("Середнє відхилення = ", str(round(Result)))

    f.write("\nСтандартне відхилення = " + str(round(sqrt(result))))
    f.write("\nСереднє відхилення = " + str(round(Result)))
#Zavd 3 function
def zavd3():
    sum = 0
    result = []
    for i in rating:
        sum += i
    a = np.array([[100, 1, ], [(sum / lens), 1, ]])
    #|100 = 100*a + b
    #|95 = 74.2*a + b
    x = solve(a, np.array([100, 95]))
    for i in range(lens):
        result.append(round(x[0] * rating[i] + x[1]))
    print("Старі оцінки: " + str(rating))
    f.write("\nСтарі оцінки: " + str(rating))

    print("\ny = " + str(x[0]) + "*x + " + str(x[1]))
    f.write("\ny = " + str(x[0]) + "*x + " + str(x[1]))

    print("\nНові оцінки: " + str(result))
    f.write("\nНові оцінки: " + str(result))
#Zavd 4 function
def zavd4():
    print("Діаграма стовбур-листя")
    print("-----------------------")

    f.write("\nДіаграма стовбур-листя")
    f.write("\n-----------------------")

    i = min(rating)

    while i <= max(rating):
        mas = []
        for j in range(lens):
            if i < rating[j] < i + 10:
                mas.append(rating[j] % 10)
            elif rating[j] == i:
                mas.append(0)
        if len(mas) != 0:
            print(str(i / 10) + " \t| " + str(mas))
            f.write("\n" + str(i / 10) + " \t| " + str(mas))
        i += 10
    print("Ключ = " + str(rating[0]))
    f.write("\nКлюч = " + str(rating[0]))
#Zavd 5 function
def zavd5():
    plt.boxplot(rating)
    plt.grid()
    plt.show()

f = open("answer.txt", "w")
rating = []
for i in open("input.txt"):
    rating.append(int(i.strip()))
rating = np.delete(rating, 0)

lens = len(rating)
rating = sorted(rating)

print("Послідовність: ", *rating)
f.write("Послідовність: " + str(rating))

print("\nЗавдання 1:")

Q1 = zavd1(1 / 4)
Q3 = zavd1(3 / 4)
P90 = zavd1(0.9)

print("Q1 = ", Q1)
print("\nQ3 = ", Q3)
print("\nP90 = ", P90)

f.write("\nQ1 = ")
f.write(str(Q1))
f.write("\nQ3 = ")
f.write(str(Q3))
f.write("\nP90 = ")
f.write(str(P90))
print("\nЗавдання 2:")
zavd2()
print("\nЗавдання 3:")
zavd3()
print("\nЗавдання 4:")
zavd4()
print("\nЗавдання 5:")
zavd5()
f.close()