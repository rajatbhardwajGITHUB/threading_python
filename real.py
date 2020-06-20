# this script will scan for images from a webpage and than 
# store it in a list 
# than download those images 
from html.parser import HTMLParser
import requests
from urllib import response, request, parse
import time 
import concurrent.futures



# geting the html from the site

req = request.urlopen('https://www.askpython.com/')

if req.getheader('content-type') == 'text/html' or 'text/css':
    html_byte = req.read()
    html_string = html_byte.decode('utf-8')
    #print(html_string)

class source_finder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.list = []
        #self.base = base_url

    def handle_starttag(self, tag, attrib):
        if tag == 'img':
        
            for (attr, value) in attrib:
                if attr == 'src':
                    
                    self.list.append(value)

fu = source_finder()
fu.feed(html_string)
print(fu.list)

t1 = time.perf_counter()
def download_image(url):
    img_bytes = requests.get(url).content
    img_name = url.split('/')[7]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as image_file:
        image_file.write(img_bytes)
        print(f'{img_name} was downloaded....')

# context manager
#for i in fu.list:
   # download_image(i)
with concurrent.futures.ThreadPoolExecutor() as exe:
    exe.map(download_image, fu.list)

t2 = time.perf_counter()
print(f'THE CODE FINISHED IN {round(t2-t1)} seconds .....')

