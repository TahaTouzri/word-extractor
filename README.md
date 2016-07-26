# word-extractor
This is an implementation of an algorithm invented by me its purpose is to extract specific word from phrases.
#example of usage
1-learn the algorithm:<br>
  -delete the learnedModel.p file from the project folder<br>
  -create a learn.txt file containing the learning set<br>
  -example of learn.txt:<br>
      my name is Taha#is<br>
      this is an open source project#is<br>
      I have three systers#have<br>
  -with the previous example the algorithm will extract verbs from phrases you deliver with<br>
  -start python learn.py learn.txt<br>
  <br>
2-start the algorithm<br>
  after you complete the first step, you can now use the learned model in your set of phrases, to do simply start:
  python extract.py source.txt<br>
  where source is your data file, where one line contain one phrase<br>
  the results will be displayed on the screen<br><br>
  
3-work to do:<br>
<br>
 -we planify to enhance the algorithm<br>
 -Add json interface (with flask server)<br>
