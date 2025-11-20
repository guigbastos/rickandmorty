from src.models import db
from src.models.character_model import Character

class CharacterRepository:

    def get_all_characters(self, filters=None, limit=10, offset=0):
        # try:
        #     characters = Character.query.all()
        #     return characters
        # except:
        #     db.session.rollback()
        #     raise
        if filters is None:
            filters = {}
        
        try:
            query = db.session.query(Character)
            if 'name' in filters:
                query = query.filter(Character.name.like(f'%{filters["name"]}%'))
            if 'status' in filters:
                query = query.filter(Character.status == filters['status'])
            if 'species' in filters:
                query = query.filter(Character.species == filters['species'])
            if 'gender' in filters:
                query = query.filter(Character.gender == filters['gender'])
            
            total = query.count()

            characters = query.offset(offset).limit(limit).all()

            return characters, total
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