import sqlite3
import json
from Question import Question

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

def addParticipation(paylod) :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    
    insertion_result = cur.execute(
        f"INSERT INTO PARTICIPATIONS (playerName,score) VALUES (?,?)",(paylod["playerName"],paylod["score"])
    )
    # send the request
    cur.execute("commit")
    db_connection.close()