marks = int(input('Enter the marks: '))

if 70 < marks < 80:
    print('Average')
    if 80 < marks < 90 :
        print('distinction')
    else:
        print('below average')
elif  90< marks < 100:
    print('Elite')
else:
    print('poor students')
        

    
        
