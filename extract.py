import nltk
from utilsFunctions import *
from nltk.corpus import wordnet as wn
import pickle
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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


textSourceFile = open(sys.argv[1],"r")
lines = textSourceFile.readlines()
nbrCorrect = 0
for line in lines:
	m = re.split('#', line)
	text = m[0]
	print "inpu text: "+text
	print "input model: "+m[1]
	extractedWord = extractMyWord(text,learnedModel)
	print "extracted model: "+extractedWord
	print "-----------------------------------------"
	if extractedWord.lower()==m[1].lower():
		nbrCorrect+=1
print nbrCorrect