N = float(input())
a =int(N/100)
b = int (N%100)
c = int(b/50)
d = int(b%50)
e = int(d/20)
f = int(d%20)
g = int(f/10)
h = int(f%10)
i = int(h/5)
j = int(h%5)
k = int(j/2)
l = int(j%2)
m = int(l/1)

o = int(m/0.50)
p = int(m%0.50)
q = int(p/0.25)
r = int(p%0.25)
s = int(r/0.10)
t = int(r%0.10)
u = int(t/0.05)
v = int(t%0.05)
w = int (v/0.01)
print("%d nota(s) de R$ 100,00" %a)
print("%d nota(s) de R$ 50,00" %c)
print("%d nota(s) de R$ 20,00" %e)
print("%d nota(s) de R$ 10,00" %g)
print("%d nota(s) de R$ 5,00" %i)
print("%d nota(s) de R$ 2,00" %k)
print("%d moeda(s) de R$ 1,00" %m)
print("%d moeda(s) de R$ 0.50" %o)
print("%d moeda(s) de R$ 0.25" %q)
print("%d moeda(s) de R$ 0.10" %s)
print("%d moeda(s) de R$ 0.05" %u)
print("%d moeda(s) de R$ 0.01" %w)
