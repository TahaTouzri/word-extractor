import nltk
from utilsFunctions import *
from nltk.corpus import wordnet as wn
import pickle
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
	print "input text: "+text
	print "input model: "+m[1]
	extractedWord = extractMyWord(text,learnedModel)
	print "extracted model: "+extractedWord
	print "-----------------------------------------"
	if extractedWord.lower()==m[1].lower():
		nbrCorrect+=1
print nbrCorrect
