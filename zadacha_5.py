# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

print('Введите координаты точки А')
ax = int(input('x: '))
ay = int(input('y: '))

print('Введите координаты точки B')
bx = int(input('x: '))
by = int(input('y: '))

def dictance(ax,ay,bx,by):
    temp=((bx-ax)**2)+((by-ay)**2)
    d = math.sqrt(temp)
    print(f'A ({ax},{ay}); B ({bx},{by}) -> {round(d,2)}')

dictance(ax,ay,bx,by)

