from src.models import db
from src.models.character_model import Character

class CharacterRepository:

    def get_all_characters(self):
        try:
            characters = Character.query.all()
            return characters
        except:
            db.session.rollback()
            raise

    def get_character_by_id(self, id):
        try:
            character = Character.query.get(id)
            return character
        except:
            db.session.rollback()
            raise