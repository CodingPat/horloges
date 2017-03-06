import urllib.request
import re


class Engine:
  def find_img(self,url):
    text=getsource(url)
  

  def get_source(self,url,code="ISO-8859-1"):
    page=urllib.request.urlopen(url)
    text=page.read().decode(code)
    return text
    
  def find_url(self,text,base_url):
    
    links=re.findall(r'<a HREF[^>]+>',text)
  
    for i in range(len(links)):
      #strip tags and add base_url
      new_string=links[i].replace('<a HREF=','').replace('>','')
      new_string=base_url+new_string
      links[i]=new_string
      
    return links
    
  def find_images(self,text):
    images=re.findall(r'<img src[^>]+>',text)
    #to do : verify if jpg
    for i in range(len(images)):
      images[i]=re.findall(r'http.*jpg',images[i])[0]
    #delete elements=null
    return images
    
  def get_url():
    #strip tags
    pass
    
    

my_engine=Engine()
base_url="http://www.ranfft.de"
text=my_engine.get_source("http://www.ranfft.de/cgi-bin/bidfun-db.cgi?10&ranfft&0&2uswk")
urls=my_engine.find_url(text,base_url)

for url in urls:
  print(url)

#####debug : test only 10 first urls  
#for i in range(2):
#  url=urls[i]
#  try:
#    print(url)
#    text=my_engine.get_source(url)
#    print(text)
#    images=my_engine.find_images(text)
#    print(images)
#    #break#debug = check only first valid url
#  except:
#    print("error handling url")
  
  