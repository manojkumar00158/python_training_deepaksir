import random

def tuple_rand(list_1):
    
    for j in range(10):
        
        r = random.randint(1,20)
        
        list_1.append(r)
        
        if type(list_1) ==  list:
            
            tuple_ = tuple(list_1)
            
    print(f'randomsied tuple is {tuple_}\n')
    
    if type(tuple_) == tuple:
        
        d={}
        
        for i in tuple_:
            
            d[i]=random.randint(1,20)
            
        print(f'coverting tuple into dictionory with keys as each item in tuple{d}\n')
    
            
            
            
    
            
             

if __name__ == '__main__':
    
    for i in range(1,21):
        list_1 = []
        tuple_rand(list_1)
    
    
    

