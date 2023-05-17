import sqlite3
import json
from datetime import datetime

def deleteAllParticipations() :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    insertion_result = cur.execute(
        f"DELETE FROM PARTICIPATIONS"
    )
    # send the request
    cur.execute("commit")
    db_connection.close()

def addParticipation(payload) :
    
    if len(payload["answers"]) != 10:
        raise ValueError("Bad Request. Le nombre de réponses est incorrect.")

    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    score = 0

    for index, answer in enumerate(payload["answers"]):
        question = cur.execute("SELECT * FROM QUESTIONS WHERE position = ?", (index + 1,)).fetchone()
        if not question:
            db_connection.close()
            raise ValueError("La question {} n'a pas été trouvée.".format(index + 1))

        possible_answers = json.loads(question[5])

        if not 1 <= answer <= len(possible_answers):
            db_connection.close()
            raise ValueError("La réponse à la question {} est invalide.".format(index + 1))

        selected_answer = possible_answers[answer - 1]

        if selected_answer["isCorrect"]:
            score += 1

    current_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    insertion_result = cur.execute(
        "INSERT INTO PARTICIPATIONS (playerName, score, date) VALUES (?, ?, ?)",
        (payload["playerName"], score, current_date)
    )
    
    cur.execute("commit")
    db_connection.close()
    return score