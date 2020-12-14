def authentication():

    dict_1 = {
        'name' : '1234',
        'name1' : '12345',
        'name3' : '123456'
        }
    
    temp = 1
    
    while True:
        
        for i,j in dict_1.items():
            user_name = input('Enter user name : ')
            password = input('Enter password: ')
            
            if user_name == i and password == j :
                print('Successfully logged in')
                login = True
            else:
                print('your user name or password doesnot match the database')
                temp +=1
                if temp > 3:
                    print('maximum tries attempted..')
                    break
        
    


authentication()
            
