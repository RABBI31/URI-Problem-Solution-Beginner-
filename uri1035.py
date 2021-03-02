value = input().split()
e,f,g,h = value
a = int(e)
b = int(f)
c = int(g)
d = int(h)
if (b>c and d>a and (c+d)>(a+b) and c>0 and d>0 and (a%2==0) ):
    print(f'Valores aceitos')
else:
    print(f'Valores nao aceitos')
