'''Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
ними в 2D пространстве.
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21'''


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
import math
distans = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distans)