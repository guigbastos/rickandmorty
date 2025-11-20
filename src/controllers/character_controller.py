from flask import jsonify
from src.services.character_service import CharacterService


class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, name):
        try:
            data = self.character_service.get_all_characters()
            return jsonify(data), 200
        except Exception as e:
            print(e)
            return jsonify({
                "Erro": "Aconteceu algum erro"
            }), 500
        
    def get_character_by_id(self, id):
        try:
            data = self.character_service.get_character_by_id(id)
            return jsonify(data), 200
        except Exception as e:
            print(e)
            return jsonify({
                "Erro": "Aconteceu algum erro"
            }), 500