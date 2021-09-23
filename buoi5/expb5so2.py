import math
a = int(input('Nhap a = '))
b = int(input('Nhap b = '))
c = int(input('Nhap c = '))
if a == 0:
    print('phuong trinh bac 2 thanh bac 1 bx+c=0 ')
    if b == 0:
        print('phuong trinh vsn')
    else:
        print('phuong trinh co 1 nghiem ',(-c/b))
else:
    deta = b*b - 4*a*c
    if deta < 0:
        print('phuong trinh vo nghiem')
    elif deta == 0:
        print('phuong trinh co 1 nghiem',(-b/(2*a)))
    else:
        x1 = (-b+math.sqrt(deta))/(2*a)
        x2 = (-b-math.sqrt(deta))/(2*a)
        print('phuong trinh co 2 nghiem x1 = {}, x2 = {}'.format(x1,x2))


#for i in range(2000,3201):
#    if(i%7==0)and(i%5!=0):
#       print(i, end=' , ')




