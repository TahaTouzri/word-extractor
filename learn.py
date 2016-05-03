from utilsFunctions import wordClass,split_composite
from nltk.corpus import wordnet as wn
import pickle
import re
import sys



#---------------------------------------------------
#                   Product Class
#---------------------------------------------------

"""
f=open( "save.p", "wb" )
for tr in chosen_transformations:
	pickle.dump( tr, f )
	
f=open( "save.p", "rb" )
chosen_transformations =[]
while f:
	try:
		tr = pickle.load(f)
		chosen_transformations.append(tr)
	except:
		break
def findListInLearnedModel(l):
	print l
	score = 0
	return score"""
textSourceFile = open(sys.argv[1],"r")
lines = textSourceFile.readlines()
listWords=[]
normalizationFactor = 0
"""
for line in lines:
	m = re.split('#', line)
	everyWord = split_composite(m[0])
	for currentWord in everyWord:
		print m[0]
		print currentWord
		word = wordClass(m[0],currentWord)
		normalizationFactor+=1
		if currentWord == m[1].rstrip():
			word.setIsItAModel(True)
		else:
			word.setIsItAModel(False)
		print word
		#raw_input("continue ...")
		save = True
		for savedWord in listWords:
			if savedWord.isItLooksLikeMe(word):
				save = False
				break
		if save:
			listWords.append(word)
"""
i=0
for line in lines:
	i+=1
	print line
	print  i
	m = re.split('#', line)
	everyWord = split_composite(m[0])

	word = wordClass(m[0],m[1].rstrip())
	word.setIsItMyWord(True)
	#print word
	#raw_input("continue ...")
	save = True
	for savedWord in listWords:
		if savedWord.isItLooksLikeMe(word):
			save = False
			break
	if save:
		listWords.append(word)

textSourceFile.close()

learnedModel=open( "learnedModel.p", "wb" )
print "--------------------------------"
print "learning results"
print "--------------------------------"
for word in listWords:
	word.normalizeScore(len(lines))
	pickle.dump(word,learnedModel)
	if word.getIsItMyWord():
		print word
	
learnedModel.close()
