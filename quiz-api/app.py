from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *
import sqlite3
from manageQuestion import addQuestion, getQuestion, deleteQuestionById, deleteAllQuestions, updateQuestion
from manageParticipations import deleteAllParticipations, addParticipation
from manageGlobal import rebuildDatabase, getQuizInfo
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    token = request.headers.get('Authorization')
    try:
        token = token.split(" ")[1]
        decode_token(token)
    except:
        return 'Unauthorized', 401
    try:
        rebuildDatabase()
    except Exception as e:
        return 'Internal Server Error', 500

    return 'Ok', 200

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	result = getQuizInfo()
	return {"size": result["size"], "scores": result["score"]}, 200

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
	payload = request.get_json()
	id = addQuestion(payload)
	return {"id":id}, 200

@app.route('/questions/<int:id>', methods=['GET'])
def GetQuestionById(id):
	try:
		question = getQuestion(id,True)
	except:
		return 'Not Found', 404
	result = question.question_to_json()
	return result, 200

@app.route('/questions', methods=['GET'])
def GetQuestionByPosition():
	position = request.args.get('position')
	try:
		question = getQuestion(position,False)
	except:
		return 'Not Found', 404
	result = question.question_to_json()
	print(result)
	return result, 200

@app.route('/questions/<int:id>', methods=['DELETE'])
def DeleteQuestionById(id):
	token = request.headers.get('Authorization')
	try:
		token = token.split(" ")[1]
		print(token)
		decode_token(token)
	except:
		return 'Unauthorized', 401
	try:
		deleteQuestionById(id)
	except:
		return 'Not Found', 404
	return 'No Content', 204

@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestions():
	token = request.headers.get('Authorization')
	try:
		token = token.split(" ")[1]
		print(token)
		decode_token(token)
	except:
		return 'Unauthorized', 401
	deleteAllQuestions()
	return 'No Content', 204

@app.route('/questions/<int:id>', methods=['PUT'])
def UpdateQuestion(id):
	token = request.headers.get('Authorization')
	try:
		token = token.split(" ")[1]
		print(token)
		decode_token(token)
	except:
		return 'Unauthorized', 401
	payload = request.get_json()
	try:
		updateQuestion(id, payload)
	except:
		return 'Not Found', 404
	return 'No Content', 204

@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipations():
	token = request.headers.get('Authorization')
	try:
		token = token.split(" ")[1]
		print(token)
		decode_token(token)
	except:
		return 'Unauthorized', 401
	deleteAllParticipations()
	return 'No Content', 204

@app.route('/participations', methods=['POST'])
def PostParticipation():
	payload = request.get_json()
	try :
		score = addParticipation(payload)
	except :
		return 'Bad Request', 400

	return {"playerName":payload["playerName"],"score":score}, 200

if __name__ == "__main__":
    app.run()