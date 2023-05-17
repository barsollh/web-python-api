import sqlite3
import json
from Question import Question

def addQuestion(paylod) :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    insertion_result = cur.execute(
        f"INSERT INTO QUESTIONS (position,title,text,image,possibleAnswers) VALUES (?,?,?,?,?)",(paylod["position"],paylod["title"],paylod["text"],paylod["image"],json.dumps(paylod["possibleAnswers"]))
    )
    # send the request
    cur.execute("commit")
    db_connection.close()
    
def getQuestion(data,isId) :
    db_connection = sqlite3.connect('./database.db', timeout=30)
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    
    if isId:
        insertion_result = cur.execute(
            f"SELECT * FROM QUESTIONS WHERE id = " + str(data)
        )
    else:
        insertion_result = cur.execute(
            f"SELECT * FROM QUESTIONS WHERE position = " + data
        )
    result = cur.fetchone()
    db_connection.close()
    
    return Question( result[4], result[0], result[1], result[2], result[3], result[5])

def deleteQuestionById(id) :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    insertion_result = cur.execute(
        f"DELETE FROM QUESTIONS WHERE id = "+str(id)
    )
    # Vérification de l'existence de l'id
    if cur.rowcount == 0:
        # L'ID spécifié n'existe pas
        db_connection.rollback()
        db_connection.close()
        raise ValueError("L'ID spécifié n'existe pas dans la table.")

    # send the request
    cur.execute("commit")
    db_connection.close()

def deleteAllQuestions() :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    insertion_result = cur.execute(
        f"DELETE FROM QUESTIONS"
    )
    # send the request
    cur.execute("commit")
    db_connection.close()

def updateQuestion(id, paylod) :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    insertion_result = cur.execute(
        f"UPDATE QUESTIONS SET title = ?, text = ?, image = ?, possibleAnswers = ?, position = ? WHERE id = ?", (paylod["title"],paylod["text"],paylod["image"],json.dumps(paylod["possibleAnswers"]),paylod["position"],str(id))
    )
    # Vérification de l'existence de l'id
    if cur.rowcount == 0:
        # L'ID spécifié n'existe pas
        db_connection.rollback()
        db_connection.close()
        raise ValueError("L'ID spécifié n'existe pas dans la table.")

    # send the request
    cur.execute("commit")
    db_connection.close()