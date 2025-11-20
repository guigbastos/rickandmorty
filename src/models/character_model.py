from src.models import db, ma
from sqlalchemy.ext.hybrid import hybrid_property


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)

    character_origin = db.relationship('Locations', back_populates='character_origins', uselist=False, lazy=True, foreign_keys=[origin_id])
    character_location = db.relationship('Locations', back_populates='character_locations', uselist=False, lazy=True, foreign_keys=[location_id])

    episodes = db.relationship('Episodes', secondary='character_episode', back_populates='characters')

    def __repr__(self):
        return f"Character('{self.name}')"

    @hybrid_property
    def last_episode(self):
        return self.episodes[-1]
    
class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    type = ma.String()
    gender = ma.String()
    origin_id = ma.Integer()
    character_origin = ma.Nested('LocationsOutput')
    location_id = ma.Integer()
    character_location = ma.Nested('LocationsOutput')
    image = ma.String()
    last_episode = ma.Nested('EpisodesOutput')


character_output = CharacterOutput()
characters_output = CharacterOutput(many=True)