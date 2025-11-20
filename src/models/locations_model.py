from src.models import db, ma
from sqlalchemy.ext.hybrid import hybrid_property

class Locations(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    dimension = db.Column(db.String)

    character_origins = db.relationship('Character', back_populates='character_origin', uselist=True, lazy=True, foreign_keys='Character.origin_id')
    character_locations = db.relationship('Character', back_populates='character_location', uselist=True, lazy=True, foreign_keys='Character.location_id')

    def __repr__(self):
        return f"<Location {self.name}>"
    
    @hybrid_property
    def residents_count(self):
        return len(self.character_locations)
    
class LocationsOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()
    residents_count = ma.Integer()