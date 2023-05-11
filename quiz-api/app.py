from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *

app = Flask(__name__)
CORS(app)

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
	if payload["password"] == "flask2023":
		token = build_token()
		return {"token": token}, 200
	else:
		return 'Unauthorized', 401
	
@app.route('/questions', methods=['POST'])
def PostQuestion():
	token = request.headers.get('Authorization')
	try:
		token = token.split(" ")[1]
		print(token)
		decode_token(token)
	except:
		return 'Unauthorized', 401
	paylod = request.get_json()
	return {"id":paylod["position"]}, 200

     
#	return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()