# -*- coding: utf-8 -*-
value = input().split(" ")
a, b, c = value

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%d eh o maior" %resultado)

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
