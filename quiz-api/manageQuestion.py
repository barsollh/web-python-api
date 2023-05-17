import sqlite3
import json
from Question import Question

def addQuestion(payload) :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    # Décalage des positions des questions suivantes :
    try:
        cur.execute("SELECT id FROM QUESTIONS WHERE position >= ?", (payload["position"],))
        rows = cur.fetchall()
        for row in rows:
            cur.execute("UPDATE QUESTIONS SET position = position + 1 WHERE id = ?", (row[0],))
    except:
        db_connection.rollback()
        db_connection.close()
        raise ValueError("L'ID spécifié n'existe pas dans la table.")

    insertion_result = cur.execute(
        f"INSERT INTO QUESTIONS (position,title,text,image,possibleAnswers) VALUES (?,?,?,?,?)",(payload["position"],payload["title"],payload["text"],payload["image"],json.dumps(payload["possibleAnswers"]))
    )
    question_id = cur.lastrowid
    # send the request
    cur.execute("commit")
    db_connection.close()
    return question_id
    
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

    try:
        cur.execute("SELECT position FROM QUESTIONS WHERE id = ?", (id,))
        current_position = cur.fetchone()[0]
    except:
        db_connection.rollback()
        db_connection.close()
        raise ValueError("L'ID spécifié n'existe pas dans la table.")
    
    insertion_result = cur.execute(
        f"DELETE FROM QUESTIONS WHERE id = ?", (id,)
    )
    
    # Décalage des questions suivantes
    cur.execute(
        "UPDATE QUESTIONS SET position = position - 1 WHERE position > ?",
        (current_position,)
    )
    
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

def updateQuestion(id, payload):
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    # est ce que la position change ?
    try:
        cur.execute("SELECT position FROM QUESTIONS WHERE id = ?", (id,))
        current_position = cur.fetchone()[0]
    except:
        db_connection.rollback()
        db_connection.close()
        raise ValueError("L'ID spécifié n'existe pas dans la table.")

    # Si la position a été modifiée, on décale les positions des questions entre l'ancienne et la nouvelle position
    if current_position != payload["position"]:
        if current_position < payload["position"]:
            # Décalage vers le haut
            cur.execute(
                "UPDATE QUESTIONS SET position = position - 1 WHERE position > ? AND position <= ?",
                (current_position, payload["position"])
            )
        else:
            # Décalage vers le bas
            cur.execute(
                "UPDATE QUESTIONS SET position = position + 1 WHERE position >= ? AND position < ?",
                (payload["position"], current_position)
            )
    
    update_result = cur.execute(
        "UPDATE QUESTIONS SET title = ?, text = ?, image = ?, possibleAnswers = ?, position = ? WHERE id = ?",
        (payload["title"], payload["text"], payload["image"], json.dumps(payload["possibleAnswers"]), payload["position"], id)
    )

    cur.execute("commit")
    db_connection.close()
