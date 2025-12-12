from src.models import db
from src.models.character_model import Character

class CharacterRepository:

    def get_all_characters(self, name, limit, offset=0):
        try:
            query = Character.query

            if name:
                query = query.filter(Character.name.ilike(f'%{name}%'))
            
            character = query.limit(limit).offset(offset).all()
            return character
        except:
            db.session.rollback()
            raise

    def count_characters(self, name):
        try:
            query = Character.query
            if name:
                query = query.filter(Character.name.ilike(f'%{name}%'))
            return query.count()
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