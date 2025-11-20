from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, characters_output
from werkzeug.exceptions import NotFound


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()

    def get_all_characters(self):
        characters = self.character_repository.get_all_characters()

        data = characters_output.dump(characters)

        return {
            "data": data
        }
    
    def get_character_by_id(self, id):
        character = self.character_repository.get_character_by_id(id)

        data = character_output.dump(character)

        return {
            "data": data
        }