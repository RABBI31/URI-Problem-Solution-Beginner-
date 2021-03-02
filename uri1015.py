# -*- coding: utf-8 -*-
import math
value1 = input().split()
value2 = input().split()
x1,y1 = value1
x2,y2 = value2
distance = math.sqrt((float(x2)-float(x1))*(float(x2)-float(x1))+(float(y2)-float(y1))*(float(y2)-float(y1)))
print(f'{distance:.4f}')

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
