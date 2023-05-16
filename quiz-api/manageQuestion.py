import sqlite3
from Question import Question

def addQuestion(paylod) :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    insertion_result = cur.execute(
        f"INSERT INTO QUESTIONS (position,titre,texte,image) VALUES (?,?,?,?)",(paylod["position"],paylod["title"],paylod["text"],paylod["image"],)
    )
    # send the request
    cur.execute("commit")
    db_connection.close()
    
def getQuestion(data,isId) :
    db_connection = sqlite3.connect('./database.db', timeout=30)
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    param = str(data)
    if isId:
        insertion_result = cur.execute(
            f"SELECT * FROM QUESTIONS WHERE id = " + param
        )
    else:
        insertion_result = cur.execute(
            f"SELECT * FROM QUESTIONS WHERE position = " + param
        )
    result = cur.fetchone()
    db_connection.close()
    
    return Question( result[4], result[0], result[1], result[2], result[3])
    