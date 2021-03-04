a,b,c = map(float, input().split())
list = [a,b,c]
list.sort(reverse=True)
if((c+b)>a and (a+b)>c and (a+c)>b):
    if(a>=b+c):
        print("NAO FORMA TRIANGULO")
    if((a*a)==(b*b)+(c*c)):
        print("TRIANGULO RETANGULO")
    if((a*a)>(b*b)+(c*c)):
        print("TRIANGULO OBTUSANGULO")
    if((a*a)<(b*b)+(c*c)):
        print("TRIANGULO ACUTANGULO")
    if(a==b==c):
        print("TRIANGULO EQUILATERO")
    if(a==b!=c or a==c!=b or b==c!=a):
        print("TRIANGULO ISOSCELES")
