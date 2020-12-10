import random

n=int(input("Enter the range:"))

n1=int(input("Enter the range for randint:"))

n2=int(input("Enter the range for randint:"))

temp = 0

while True:

    list_1=[]

    for j in range(n):
        r = random.randint(n1,n2)

        if  r not in list_1 :
            list_1.append(r)

    print('Randomised list is: ',list_1)

    temp+=1
    if temp == 10:
       break
