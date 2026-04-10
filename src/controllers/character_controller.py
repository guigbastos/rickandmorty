from flask import jsonify
from src.services.character_service import CharacterService
import traceback
# from src.utils.api_response import ApiResponse



class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, name, page):
        try:
            data = self.character_service.get_all_characters(name, page)
            return jsonify(data), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify({
                "Erro": str(e)
            }), 500

    def get_character_by_id(self, id):
        try:
            data = self.character_service.get_character_by_id(id)
            return jsonify(data), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify({
                "Erro": str(e)
            }), 500