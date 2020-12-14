# Python program to count the frequency of 
# elements in a list using a dictionary 

def CountFrequency():

#creating a list with repititive items
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2,7]
	
# Creating an empty dictionary
    count = {} 
    for i in my_list:
        if my_list.count(i) > 1:
            count[i] = count.get(i, 0) + 1
    return count 

 
 

print(CountFrequency()) 
