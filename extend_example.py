
list_1 = [[1,2,3],[34,51],11,10]#coverting two dimensional to one dimensional



x = list_1[0] 

y = list_1[1]

z = list_1[2:]


x.extend(y)
x.extend(z)

print(x)


#another trail

list_2 = [[1,2],[34,51],[11,10]]
list_3 = []
for x in list_2:
    list_3.extend(x)
print(list_3)



