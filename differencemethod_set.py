#1
a = {'string1',1,2,3,4}
b = {1,2,6,(1,2)}
print(b.difference(a))#cant use set in set because of its unhashable 

#2
a = {'string1',1,2,3,4}
b = {1,2,6,1,4,7}
print(b.difference(a))#cant use list ,list of tuple,dict in a set they are unhashable

#3
a = {-5,-7,1,2,3,4}
b = {1,2,6,}
print(a.difference(b))

#4
a = {'some',1,2,3,4}
b = {1,2,6,(1,2),((1,2),(4,0))}
print(b.difference(a))

#5
a = {(12,21),1,4,7,8}
b = {1,3,6,(1,8)}
print(a.difference(b))

#6
a = set()
b = set()
print(b.difference(a))

#7
a = {1,2,3}
b = {0,7,3+2j}
print(a.difference(b))

#8
a = {0,4,4.5}
b = {2,4,5.5}
print(b.difference(a))

#9
a = {3}
b = {1,5,6}
print(a.difference(b))

#10
a = {1}
b = {(1,2)}
print(a.difference(b))
