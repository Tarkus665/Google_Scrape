# Master script for Final Project


# First step: get DHS words into a list from included .txt doc:
# (file path will vary of course)

DHSWords = []
Words = open("/Users/applestore/Desktop/Google_Scrape/DHS_words.txt", 'r')
for words in Words:
	DHSWords = Words.readlines()



# Next step is to plug those values into an image scraper:
# It will be dependent on having an "images" folder created beforehand.

