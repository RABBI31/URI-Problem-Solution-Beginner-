value = input().split()
c,d= value
a = int(c)
b = int(d)
if(b%a==0 or (a%b == 0)):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
