
#Simplest and best way to get DHS words into a list:

>>> DHSWords = []
>>> Words = open("/Users/applestore/Desktop/Google_Scrape/DHS_words.txt", 'r')
>>> for words in Words:
	DHSWords = Words.readlines()





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
 
data



 #This will return the DHS_words.txt file as a biiiiiig list


def getwordsList():
	listfile = open("/Users/applestore/Desktop/Google_Scrape/DHS_words.txt", 'r')
	linelist = listfile.readlines()
	print(linelist)
	listfile.close()


#This will **enumerate** over the list and return it as a long numbered list

def getwordsList():
	listfile = open("/Users/applestore/Desktop/Google_Scrape/DHS_words.txt", 'r')
	linelist = listfile.readlines()
	for name in enumerate(linelist):
		print(name)







	
