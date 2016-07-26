# word-extractor
This is an implementation of an algorithm invented by me its purpose is to extract specific word from phrases.
#example of usage
1-learn the algorithm:<br>
  -delete the learnedModel.p file from the project folder
  -create a learn.txt file containing the learning set
  -example of learn.txt:
      my name is Taha#is
      this is an open source project#is
      I have three systers#have
  -with the previous example the algorithm will extract verbs from phrases you deliver with
  -start python learn.py learn.txt
  
2-start the algorithm
  after you complete the first step, you can now use the learned model in your set of phrases, to do simply start:
  python extract.py source.txt
  where source is your data file, where one line contain one phrase
  the results will be displayed on the screen
  
3-work to do:

 -we planify to enhance the algorithm
 -Add json interface (with flask server)
