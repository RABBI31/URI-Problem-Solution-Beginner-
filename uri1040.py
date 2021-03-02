
n1,n2,n3,n4 = map(float,input().split())
sum = float(((n1*2)+(n2*3)+(n3*4)+(n4*1))/10)
print(f'Media: {sum:.1f}')
if(sum>=7.0):
    print("Aluno aprovado.")
elif(sum<5.0):
    print("Aluno reprovado")
elif(sum>=5.0 and sum<7.0):
    print("Aluno em exame.")
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    sum2 = float((sum + n5)/2)
    if(sum2>=5.00):
       print("Aluno aprovad.")
       print(f'Media final: {sum2:.1f}')
    else:
       print("Aluno reprovado.")
       print(f'Media final: {sum2:.1f}')

