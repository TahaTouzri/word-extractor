import nltk
from utilsFunctions import *
from nltk.corpus import wordnet as wn
import pickle
import time


def extractMyWord(text,learnedModel):
	listOfWords = split_composite(text)
	words = []
	#Create words objects
	for word in listOfWords:
		words.append(wordClass(text,word))
	bestScore = 0
	MyWord    = ""
	for word in words:
		for MyTypicalWord in learnedModel:
			if word.getList() == MyTypicalWord.getList():
				if MyTypicalWord.getScore()>bestScore:
					bestScore = MyTypicalWord.getScore()
					MyWord    = word
	return listOfWords[words.index(MyWord)]




#---------------------------------------------------
#                 Use Example
#---------------------------------------------------


#---------------------------------------------------
#                 Load learned Model
#---------------------------------------------------

f=open( "learnedModel.p", "rb" )
learnedModel =[]
while f:
	try:
		obj = pickle.load(f)
		learnedModel.append(obj)
	except:
		break
#call extractMyWord function
		
text = "PiPO X6s Quad-Core TV Box (EU)"
print extractMyWord(text,learnedModel)