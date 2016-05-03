import unittest
from utilsFunctions import *



def test_split_composite():
	r0=split_composite("hello word")
	assert r0==["hello","word"]
	
	
def test_isItBeforeSpecificWord():
	assert isItBeforeSpecificWord("word","specificWord",["word","specificWord"])
	
	
def test_isItAfterSpecificWord():
	assert isItAfterSpecificWord("word","specificWord",["specificWord","word"])
	assert not isItAfterSpecificWord("word","specificWord",["NOTspecificWord","word"])
	
	
def test_isItBeforeAwordThatStartsWithANumber():
	assert isItBeforeAwordThatStartsWithANumber("word",["word","1startsWithIt"])
	assert not isItBeforeAwordThatStartsWithANumber("word",["word","startsWithOut1"])
	
	
def test_isItAfterAwordThatStartsWithANumber():
	assert isItAfterAwordThatStartsWithANumber("word",["1startsWithIt","word"])
	assert not isItAfterAwordThatStartsWithANumber("word",["word","startsWithOut1"])
	
def test_isItSignificantWord():
	assert isItSignificantWord("dog")
	assert not isItSignificantWord("iplsg")
	
def test_isItStartsWithANumber():
	assert isItStartsWithANumber("1startwithANumber")
	assert not isItStartsWithANumber("NotStartinwith1Number")
	
def test_doesItContainANumber():
	assert doesItContainANumber("h4tt")
	assert not doesItContainANumber("NoNumber")

def test_isItContainOneWord():
	assert isItContainOneWord("word")
	assert not isItContainOneWord("two words")

def test_doesItStartsWithUpperCase():
	assert doesItStartsWithUpperCase("Yes")
	assert not doesItStartsWithUpperCase("no")
	
def test_isItANoun():
	assert isItANoun("door","open the door")
	assert not isItANoun("open","open the door")

def test_isItANAdj():
	assert isItANAdj("good","good boy")
	assert not isItANAdj("boy","good boy")
	
def test_isItAVerb():
	assert isItAVerb("go","go to the home")
	assert not isItAVerb("home","go to the home")