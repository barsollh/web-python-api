import json


class Question:
    def __init__(self, id, position, title, text, image, possibleAnswers):
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        self.possibleAnswers = possibleAnswers

    def __str__(self):
        return f"id: {self.id}\nPosition: {self.position}\ntitle: {self.title}\ntext: {self.text}\nImage: {self.image}\nPossibleAnswers: {self.possibleAnswers}"
    
    def question_to_json(self):
        return {
            'id' : self.id,
            'position': self.position,
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'possibleAnswers': json.loads(self.possibleAnswers)
        }
    
    def json_to_question(json_str):
        json_dict = json.loads(json_str)
        id = json_dict.get('id')
        position = json_dict.get('position')
        title = json_dict.get('title')
        text = json_dict.get('text')
        image = json_dict.get('image')
        possibleAnswers = json.dumps(json_str.get('possibleAnswers'))
        return Question(id, position, title, text, image, possibleAnswers)
