import sqlite3
import datetime

def rebuildDatabase() :
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    
    # Réinitialisation des données stockées
    cur.execute("DELETE FROM QUESTIONS")
    cur.execute("DELETE FROM PARTICIPATIONS")
    cur.execute("DELETE FROM sqlite_sequence WHERE name='QUESTIONS'")
    cur.execute("DELETE FROM sqlite_sequence WHERE name='PARTICIPATIONS'")
    
    # Création de la table QUESTIONS
    cur.execute('''CREATE TABLE IF NOT EXISTS QUESTIONS (
        position INTEGER NOT NULL,
        title TEXT NOT NULL,
        text TEXT NOT NULL,
        image TEXT,
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        possibleAnswers TEXT
    )''')

    # Création de la table PARTICIPATIONS
    cur.execute('''CREATE TABLE IF NOT EXISTS PARTICIPATIONS (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        playerName TEXT NOT NULL,
        score INTEGER NOT NULL,
        date TEXT NOT NULL
    )''')
    
    cur.execute("commit")
    db_connection.close()
    
def getQuizInfo():
    db_connection = sqlite3.connect('./database.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    # Récupération des scores de toutes les participations
    cur.execute("SELECT playerName, score, date FROM PARTICIPATIONS ORDER BY score DESC")
    rows = cur.fetchall()
    
    scores = []
    for row in rows:
        playerName = row[0]
        score = row[1]
        date = row[2]
        #formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
        score_details = {"date": date, "playerName": playerName, "score": score}
        scores.append(score_details)

    # Récupération du nombre total de participations
    cur.execute("SELECT COUNT(*) FROM QUESTIONS")
    size = cur.fetchone()[0]

    db_connection.close()

    return {"size": size, "score": scores}
