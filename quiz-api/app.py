from flask import Flask, request
from flask_cors import CORS
import jwt
from jwt_utils import *

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'clefpipi'

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def PostLogin():
	payload = request.get_json()
	if payload["password"]=="flask2023" :
		token=build_token()
		return {"token": token}, 200
	else:
		return {}, 401

@app.route('/questions', methods=['POST'])
def AddQuestion():
	token = request.headers.get('Authorization')
	
	try:
		decode_token(token)
	except :
		return 'unauthorize', 401

	payload = request.get_json()
		




if __name__ == "__main__":
    app.run()