import requests
def foo(url):
    url_ =  requests.get(url,verify=False)
    print(url_)
    if  url_.status_code == 200:
        print (type(url_.text))
    filename = url.split('.')[1]+'.html'
    with open(filename,'w') as geeksforgeeks_page:
        geeksforgeeks_page.write(url_.text)
        

if __name__ == '__main__':
    url = 'http://www.geeksforgeeks.com'
    foo(url)
