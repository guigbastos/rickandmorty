from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, characters_output
from werkzeug.exceptions import NotFound


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self, name, page):
        limit = 20
        offset = (page - 1) * limit
        characters = self.character_repository.get_all_characters(name, limit, offset)
        total_items = self.character_repository.count_characters(name)

        if total_items > 0:
            total_pages = (total_items + limit - 1) // limit
        else:
            total_pages = 1

        data = characters_output.dump(characters)

        return {
            "data": data,
            "meta": {
                "current_page": int(page),
                "total_pages": int(total_pages),
                "total_items": int(total_items)
            }
        }
        
    
    def get_character_by_id(self, id):
        character = self.character_repository.get_character_by_id(id)

        if not character:
            raise NotFound("Personagem não encontrado")

        data = character_output.dump(character)

        return {
            "data": data
        }