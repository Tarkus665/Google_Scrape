
#Simplest and best way to get DHS words into a list:

>>> DHSWords = []
>>> Words = open("/Users/applestore/Desktop/Google_Scrape/DHS_words.txt", 'r')
>>> for words in Words:
	DHSWords = Words.readlines()




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







	
