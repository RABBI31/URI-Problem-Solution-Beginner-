import math
value = input().split()
a,b,c= value
root = float(2*float(a))
squarrot = float((float(b)*float(b))-(4*float(a)*float(c)))

if root!=0 and  squarrot>0:
    r1 = float((-(float(b))+(math.sqrt(float(squarrot))/float(root))))
    r2 = float((-(float(b))-(math.sqrt(float(squarrot)))/float(root)))
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
else:
    print("Impossivel calcular")

