import nltk
from utilsFunctions import *
from nltk.corpus import wordnet as wn
import pickle
from flask import Flask, jsonify, Response, request,render_template, redirect, url_for
from werkzeug.utils import secure_filename
import sys
import os
import time
reload(sys)
sys.setdefaultencoding('utf8')


UPLOAD_FOLDER = './learn'
ALLOWED_EXTENSIONS = set(['txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/learn.html', methods=['GET', 'POST'])
def upload_file():
    def sendData(data):
        return data
    message_to_user=""
    error_message  =""
    if request.method == 'POST':
        form = request.form
        # check if the post request has the file part
        if 'file' not in request.files:#start learning button
            message = '{"error":"No file selected"}'
            return Response(message)
        else:
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                #flash('No selected file')
                message = '{"error":"No file selected"}'
                return Response(message)
                #return redirect(request.url)
            elif not allowed_file(file.filename):
                message = '{"error":"File format not supported"}'
                return Response(message)
            elif file and allowed_file(file.filename):
                message = '{"info":"File uploaded successfully"}'
                filename = secure_filename(file.filename)
                file.save(os.path.join(sys.path[0],app.config['UPLOAD_FOLDER'], filename))
                return Response(message)
            #return redirect(url_for('uploaded_file',filename=filename))
    return render_template("/learn.html",message_to_user=message_to_user,error_message=error_message)

def file_verification():
	for i in range(101):
		time.sleep(0.1)
		print i
		ev   = ServerSentEvent(i)
		yield ev.encode()
	ev   = ServerSentEvent(str("end"))
	yield ev.encode()

@app.route('/verification_stream', methods=['GET', 'POST'])
def verification_stream():
	print "------------------------------------"
	print "in the verification stream view"
	return Response(file_verification(), mimetype="text/event-stream")

@app.route('/generation_stream', methods=['GET', 'POST'])
def generation_stream():
	print "------------------------------------"
	print "in the generation stream view"
	return Response(learnAlgorithm("learn.txt"), mimetype="text/event-stream")

if __name__ == "__main__":
	app.debug = True
	app.run(threaded=True)
