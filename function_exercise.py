#function takes 3 parameters two default  and one keyword parameter

def function(a,b,num):
    
#taking a,b parameters in dictionary format
    
    dict_1 = {a : b}
    
    print(dict_1)
    
#length of value in the dict_1
    
    print(f'length of "b"  value in dictionary {len(dict_1[a])}')
       
    len_of_b = dict_1[a]
    
    for i in len_of_b:
                      
#count of each character in value of dict_1
        
        print(f'count of "{i}"  is  "{len_of_b.count(i)}" ')
            
    if num.isnumeric() == True:

        c = int(num)

        if c > 1:
            print(c,'is an integer')
            
        for j in range(2,c):
            
#not prime number            
            if (c % j) == 0:
                print(c, "is not a prime number")
                
#even number                
                if (c % 2) == 0:
                    print(c,"is even number" )
                    
#odd number                    
                else:
                    print(c,"is odd number")
#divisible by 3                    
                if (c % 3) == 0:
                    print(c,"is divisble by 3")
                    
#divisible by 5                    
                elif (c % 5) == 0:
                    print(c,"is divisible by 5")
                          
                break
#prime number            
            else:
                print(c, "is a prime number")
                
#even number                
                if (c % 2) == 0:
                    print(c,"is even number" )
                    
#prime number                    
                else:
                    print(c,"is odd number")
      
                break

    else:
        print('enter integer...!')
        
    
    
    
            
    
if __name__ == '__main__':
    a = 'name'
    b = 'deepak'
    function(a,b,num = input('enter any number: '))
