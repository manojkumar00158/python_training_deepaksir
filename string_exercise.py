statement = input('enter the sentences: ')

if statement:

    lower_ = statement.lower()

    vowels = 'a','e','i','o','u'

    numbers = '1','2','3','4','5','6','7','8','9'

    
    symbol = '@Αß東&§¡©'


    for letter in lower_:
        
        statement_ = lower_.find(letter,lower_.index(letter)+1,len(lower_))
    
        if statement_ == -1 :
                
                if letter in vowels:
                        
                    print(f'unique character is {letter} and this is vowel and ord is {ord(letter)}')

 
                elif letter in symbol:

                    print(f'unique character is {letter} and {symbol.encode()} it is a symbol' )

                elif letter in numbers:

                    print('')
                    
                else:

                    print(f'unique character is {letter} and this is consonent and ord is {ord(letter)}')
                    
   
else:

    print("please enter something.")

        
        
        
