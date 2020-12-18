import requests
def foo(url):
    url_ =  requests.get(url)
    print(url_)
    if  url_.status_code == 200:
        print (type(url_.text))
    filename = url.split('.')[1]+'.html'
    with open(filename,'w') as icc_page:
        icc_page.write(url_.text)
        

if __name__ == '__main__':
    url = 'http://www.icc.com'
    foo(url)
