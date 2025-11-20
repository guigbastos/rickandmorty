from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, characters_output
from werkzeug.exceptions import NotFound


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, params):
        # characters = self.character_repository.get_all_characters()

        # data = characters_output.dump(characters)

        # return {
        #     "data": data
        # }

        limit = int(params.pop('limit', 10))
        offset = int(params.pop('offset', 0))

        characters, total = self.character_repository.get_all_characters(params, limit, offset)

        data = characters_output.dump(characters)

        return {
            "data": data,
            "meta": {
                "limit": limit,
                "offset": offset,
                "total": total,
                "pages": (total + limit - 1) // limit if limit > 0 else 0
            }
        }
        
    
    def get_character_by_id(self, id):
        character = self.character_repository.get_character_by_id(id)

        data = character_output.dump(character)

        return {
            "data": data
        }