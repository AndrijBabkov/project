import numpy as np
from math import *
#Додаткові функції
def P(b, total):
    return (b / total)
def A(n, m):
    result = (np.math.factorial(n)/np.math.factorial(n - m))
    return result
def dob_fact(a, p, m, n):
    result = (p / n) * fact(a, m)
    return result
def fact(n, m):
    result = (np.math.factorial(n) * np.math.factorial(m-3))/(np.math.factorial(m)*np.math.factorial(n-3))
    return result
#Вирішення завдань
def zavd1(b, br, r, bl):
    print("Задача 1:")
    total = b + br + r + bl
    print("Ймовірність, що навмання взята коробка виявиться чорною =", round((P(b, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться коричневою =", round((P(br, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться червоною =", round((P(r, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться синьою =", round((P(bl, total)), 2))
    print("Ймовірність, що навмання взята коробка виявиться червоного або синього кольору =", (P(bl, total) + P(r, total)))
def zavd2(n, n1, m):
    print("\Задача 2:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("Ймовірність, що серед навмання вибраних двох співробітників, хоча б один буде консультантом =", round(((A1 - A2) / A1), 2))
def zavd3(n, n1, m):
    print("\Задача 3:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("Ймовірність, що серед вибраних фахівців буде принаймні один із родичів. =", round(((A1 - A2) / A1), 2))
def zavd4(p1, p2, p3, p4):
    print("\Задача 4:")
    print("Ймовірність того, що цей товар призначений для п’ятого відділу =", round(((1 - (p1 + p2 + p3 + p4))), 2))
def zavd5(p1, a1):
    print("\Задача 5:")
    print("Ймовірність прибуття двох розбіркових потягів по двох сусідніх коліях =", round((((p1/a1) * ((p1-1)/(a1-1)))), 2))
def zavd6(p1, p2):
    print("\Задача 6:")
    print("Ймовірність того, що виготовлення виробу першого ґатунку даним станком =", round(((p1 * p2)), 2))
def zavd7(p1, p2, p3, p4, a1, a2, a3, a4, m, n):
    print("\Задача 7:")
    b = dob_fact(a1, p1, m, n) + dob_fact(a2, p2, m, n) + dob_fact(a3, p3, m, n) + dob_fact(a4, p4, m, n)
    print("Ймовірність того, що цей студент підготовлений: \n\t\tа) відмінно = ", round((dob_fact(a1, p1, m, n) / b), 2))
    print("\t\tб) погано = ", round((dob_fact(a4, p4, m, n) / b), 3))
def zavd8(p1, p2, p3, a1, a2, a3):
    print("\Задача 8:")
    print("Ймовірність того, що навмання взята деталь стандартна =", round((((p1*a1) + (p2*a2) + (p3*a3))), 2))
def zavd9(p1, p2, p3, a1, a2, a3):
    print("\Задача 9:")
    print("Ймовірність того, що пацієнт був хворий на перитоніт =", round((((p2 * a2)/((p1 * a1) + (p2 * a2) + (p3 * a3)))), 2))
def zavd10(p1, p2, a1, a2):
    print("\Задача 10:")
    print("Ймовірність того, що прилад зібраний фахівцем високої кваліфікації =", round((((p1 * a1) / ((p1 * a1) + (p2 * a2)))), 2))

zavd1(40, 26, 22, 12)
zavd2(10,2,2)
zavd3(10,8,3)
zavd4(0.15, 0.25, 0.2, 0.1)
zavd5(80, 120)
zavd6(0.9, 0.8)
zavd7(3, 4, 2, 1, 20, 16, 10, 5, 20, 10)
zavd8(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)
zavd9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)
zavd10(0.3, 0.7, 0.9, 0.8)