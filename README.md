# word-extractor
This is an implementation of an algorithm invented by me its purpose is to extract specific word from phrases.
#example of usage
1-learn the algorithm:<br>
&nbsp;-delete the learnedModel.p file from the project folder<br>
&nbsp;-create a learn.txt file containing the learning set<br>
&nbsp;-example of learn.txt:<br>
&nbsp;&nbsp;my name is Taha#is<br>
&nbsp;&nbsp;this is an open source project#is<br>
&nbsp;&nbsp;I have three systers#have<br>
&nbsp;-with the previous example the algorithm will extract verbs from phrases you deliver with<br>
&nbsp;-start python learn.py learn.txt<br>
  <br>
2-start the algorithm<br>
&nbsp;after you complete the first step, you can now use the learned model in your set of phrases, to do simply start:<br>
&nbsp;python extract.py source.txt<br>
&nbsp;where source is your data file, where one line contain one phrase<br>
&nbsp;the results will be displayed on the screen<br><br>
  
3-work to do:<br>
<br>
&nbsp;-we planify to enhance the algorithm<br>
&nbsp;-Add json interface (with flask server)<br>
