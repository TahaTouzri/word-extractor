import string
import re
import nltk
from nltk.corpus import wordnet as wn

#-------------------------------------------------------
#            Functions used by the Model finder
#-------------------------------------------------------
def split_composite(w):
	try:
		m = re.split(', | & | and | ', w)
		return [s.lower() for s in m]
	except:
		return []

def isItBeforeSpecificWord(word,specificWord,wordsList):
	for i in xrange(len(wordsList)-1):
		if (wordsList[i].lower()==word.lower())and(wordsList[i+1].lower()==specificWord.lower()):
			return True
	return False

def isItAfterSpecificWord(word,specificWord,wordsList):
	for i in xrange(len(wordsList)-1):
		if (wordsList[i].lower()==specificWord.lower())and(wordsList[i+1].lower()==word.lower()):
			return True
	return False
def isItBeforeAwordThatStartsWithANumber(word,wordsList):
	try:
		nextWord = wordsList[wordsList.index(word)+1]
		if nextWord[0].isdigit():
			return True
		else:
			return False
	except:
		return False

def isItAfterAwordThatStartsWithANumber(word,wordsList):
	try:
		nextWord = wordsList[wordsList.index(word)-1]
		if nextWord[0].isdigit():
			return True
		else:
			return False
	except:
		return False

def isItSignificantWord(word):
	synts = wn.synsets(word)
	if synts:
		return True
	else:
		return False


def isItStartsWithANumber(word):
	try:
		return word[0].isdigit()
	except:
		return False

def doesItContainANumber(word):
	return any(char.isdigit() for char in word)


def isItContainOneWord(word):
	l = split_composite(word)
	return len(l)==1


def doesItStartsWithUpperCase(word):
	return word[0].upper()==word[0]

def isItANoun(word,text):
	significantText = nltk.word_tokenize(text)
	result          = nltk.pos_tag(significantText)
	for i in result:
		if i[0].lower()==word.lower() and i[1]=="NN":
			return True
	return False

def isItANAdj(word,text):
	significantText = nltk.word_tokenize(text)
	result          = nltk.pos_tag(significantText)
	for i in result:
		if i[0].lower()==word.lower() and i[1]=="JJ":
			return True
	return False

def isItAVerb(word,text):
	significantText = nltk.word_tokenize(text)
	result          = nltk.pos_tag(significantText)
	for i in result:
		if i[0].lower()==word.lower() and i[1]=="VB":
			return True
	return False

def whatIsTheRelativePositionOfTheWord(word,text):
	l=split_composite(text)
	l1=split_composite(word)
	return float(l.index(l1[0])+1)/len(l)

def isItAColor(word):
	global colorsList
	if word.lower().rstrip() in colorsList:
		return True
	else:
		return False
#------------------------------------------------------
#            The highest level extract function
#------------------------------------------------------
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

#-------------------------------------------------------
#            		Word Class
#-------------------------------------------------------
class wordClass():
	def __init__(self,text,word):
		self.list       = []
		self.text       = text
		self.score      = 1
		self.isItMyWord = False
		self.word       = word
	def __str__(self):
		l0 = "--------------------"
		l1 = self.word
		l2 = "self.list = " + str(self.getList())
		l3 = "self.score = "+str(self.getScore())
		l4 = "is it My Word = "+str(self.getIsItMyWord())
		return l0+"\n"+l1+"\n"+l2+"\n"+l3+"\n"+l4
	def computeList(self):
		textList = split_composite(self.getText())
		word     = self.getWord()
		text     = self.getText()
		l=[isItBeforeSpecificWord(word,"model",textList),isItAfterSpecificWord(word,"model",textList),isItBeforeAwordThatStartsWithANumber(word,textList),
		isItAfterAwordThatStartsWithANumber(word,textList),isItSignificantWord(word),isItStartsWithANumber(word),doesItContainANumber(word),isItANoun(word,text),isItANAdj(word,text),isItAVerb(word,text)]
		return l
	def getList(self):
		if self.list:
			return self.list
		else:
			self.list = self.computeList()
			return self.list
	def getText(self):
		return self.text
	def getScore(self):
		return self.score
	def getWord(self):
		return self.word
	#This function mesure the distance, this function is used only during learning
	def isItLooksLikeMe(self,wordCharc):
		if self.getList() == wordCharc.getList() and self.getIsItMyWord()==wordCharc.getIsItMyWord():
			self.score+=1
		return self.list == wordCharc.getList() and self.getIsItMyWord()==wordCharc.getIsItMyWord()
	def normalizeScore(self,normalizationFactor):
		self.score=float(self.score)/normalizationFactor
	def setIsItMyWord(self,isItMyWord):
		self.isItMyWord = isItMyWord
	def getIsItMyWord(self):
		return self.isItMyWord
