from math import *
import matplotlib.pyplot as plt
f = open('input.txt')
rating = []
for line in f:
    temp = int(line)
    rating.append(temp)
N = rating[0]
del(rating[0])
#таблиця частот
print("i"," - ","Xi")
for i in range(len(rating)):
    print(i+1, " - ", rating[i])
maxCount = max(rating)
top = rating.index(maxCount) + 1
print("Найчастіше: ", top)
#Мода та медіана вибірки
moda = [0]*10000
for i in range(len(rating)):
    moda[rating[i]] += 1
maxCount = max(moda)
modaNumber = moda.index(maxCount)
mediana = 0
if N % 2 == 0:
    mediana = (rating[N//2] + rating[N//2 - 1]) / 2
else:
    mediana = rating[N//2]
print("Мода: ", modaNumber, "Медіана: ", mediana)
#Дисперсія та середнє квадратичне відхилення
probability = []
for i in range(len(rating)):
    temp = rating[i]/sum(rating)
    probability.append(temp)
firstSum = secondSum = 0
for i in range(len(rating)):
    firstSum += rating[i]**2 * probability[i]
    secondSum += rating[i] * probability[i]
disp = firstSum - secondSum**2
vidh = sqrt(disp)
print("Дисперсія: ", disp, "СКВ: ", vidh)
#Гістограма частот
plt.bar(range(len(rating)), rating)
plt.xlabel("Фільм")
plt.ylabel("«Частота перегляду»")
plt.show()
