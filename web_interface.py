import nltk
from utilsFunctions import *
from nltk.corpus import wordnet as wn
import pickle
from flask import Flask, jsonify, Response, request,render_template
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


f=open( "learnedModel.p", "rb" )
learnedModel =[]
while f:
	try:
		obj = pickle.load(f)
		learnedModel.append(obj)
	except:
		break


@app.route("/extract.html", methods=['GET', 'POST'])
def extract():
    global learnedModel
    if request.method == 'POST':
        if not request.json or not 'text' in request.json:
            abort(400)
        text = request.json['text']
        word  = extractMyWord(text,learnedModel)
    else:
        text  = "Hy dear I'm here"
        word  = extractMyWord(text,learnedModel)

    tasks = [
        {
            'text':text,
            'word':word
        }
    ]
    return jsonify({'tasks': tasks})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/learn.html", methods=['GET', 'POST'])
def learn():
    return render_template('learn.html')

if __name__ == "__main__":
	app.debug = True
	app.run(threaded=True)
