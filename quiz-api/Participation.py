import json


class Participation:
    def __init__(self, id, playerName, score):
        self.id = id
        self.playerName = playerName
        self.score = score

    def __str__(self):
        return f"id: {self.id}\nPlayerName: {self.playerName}\nScore: {self.score}\n"
    
    def question_to_json(self):
        return {
            'id' : self.id,
            'playerName': self.playerName,
            'score': self.score,
        }
    
    def json_to_question(json_str):
        json_dict = json.loads(json_str)
        id = json_dict.get('id')
        playerName = json_dict.get('playerName')
        score = json_dict.get('score')
        return Participation(id, playerName, score)
