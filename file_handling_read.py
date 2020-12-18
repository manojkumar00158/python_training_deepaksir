from web_data_extraction import website

def web(url):

    website(url)

    filename = url.split('.')[1]+'.html'

    with open(filename,'r') as google_page:
        
        greadlines = str(google_page.readlines())
        
        gdata = greadlines.split(',')
        
        set_ = set()
        
        for value in gdata:
            
            if value.isdigit():
                
                set_.add(int(value))
                
        list_ = list(set_)
        
        print(f'before:{set_}\n\n\n')
        
        newlist_ = []
        
        tuple_ = ()
        for value in list_:
            if value%2 == 0:
                list_.remove(value)
            if value%3 == 0:
                list_.pop()
            if value%4 == 0:
                newlist_.append(value)
        
        print(f'after:{tuple(newlist_)}')

if __name__ == '__main__':
    url = 'http://www.google.com'
    web(url)
    
    
        
            
                
            


        

