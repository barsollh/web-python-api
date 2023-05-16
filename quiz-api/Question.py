import json


class Question:
    def __init__(self, id, position, titre, texte, image=None):
        self.id = id
        self.position = position
        self.titre = titre
        self.texte = texte
        self.image = image

    def __str__(self):
        return f"id: {self.id}\nPosition: {self.position}\nTitre: {self.titre}\nTexte: {self.texte}\nImage: {self.image}"
    
    def question_to_json(self):
        return json.dumps(self.__dict__)

    def json_to_question(json_str):
        json_dict = json.loads(json_str)
        id = json_dict.get('id')
        position = json_dict.get('position')
        titre = json_dict.get('titre')
        texte = json_dict.get('texte')
        image = json_dict.get('image')
        return Question(position, titre, texte, image)
