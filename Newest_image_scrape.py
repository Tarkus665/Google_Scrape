


import urllib.request
user_agent = 'Mozilla'


page = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=&bih=&q=yunocchi&btnG=Search+by+image'
headers = {'User-Agent':user_agent,}

request = urllib.request.Request(page,None,headers)
response = urllib.request.urlopen(request)

my_picture = response.read()

for line in my_picture:
    if line.find('img src'):
        picture1 = line[7 + line.find('img src'):line.find('">')]



fout = open(filename, "wb")
fout.write(my_picture)
fout.close()





