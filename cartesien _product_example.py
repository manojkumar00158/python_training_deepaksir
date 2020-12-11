list_1 = ['color','white','black']#taking the colors of t-shirts as input

list_2 = ['short','medium','large','xl']#taking sizes of t-shirts as input 

for color in list_1: 
    
    for size in list_2:
        
#using cartesien product asking to give output as the combinations of color and size of t-shirts we have
        
        print(color,size) 
        
#using list comprehension for the above input giving the same output but in reverse order 

list_3 = [ (color,size) for color in list_1 for size in list_2]

list_3.reverse()#used reverse method in lists

print(list_3)

