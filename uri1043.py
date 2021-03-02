a,b,c = map(float, input().split())
if((c+b)>a and (a+b)>c and (a+c)>b):
    triarea = a+b+c
    print(f'Perimetro = {triarea:.1f}')
else:
    truarea=((a+b)/2)*c
    print(f'Area = {truarea:.1f}')
