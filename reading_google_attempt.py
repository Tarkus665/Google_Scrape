#This will return the data from a google image search for "yunocchi"
	#(replace 'yunocchi' with whatever)
# but will also crash Python...	

import urllib.request
   
user_agent = 'Mozilla'
page = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=&bih=&q=yunocchi&btnG=Search+by+image'
headers = {'User-Agent':user_agent,}
request = urllib.request.Request(page,None,headers)
response = urllib.request.urlopen(request)
data = response.read()
 

