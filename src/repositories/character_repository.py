from src.models import db
from src.models.character_model import Character

class CharacterRepository:

    def get_all_characters(self, name=None, page=1, limit=20, offset=0):
        try:
            if page and page > 1:
                offset = (page - 1) * limit
            
            query = Character.query

            if name:
                query = query.filter(Character.name.ilike(f'%{name}%'))
            
            character = query.limit(limit).offset(offset).all()
            return character
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