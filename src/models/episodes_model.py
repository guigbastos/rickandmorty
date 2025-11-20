from src.models import db, ma

class Episodes(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    air_date = db.Column(db.String)
    episode = db.Column(db.String)

    characters = db.relationship('Character', secondary='character_episode', back_populates='episodes', uselist=True, lazy=True)

    def __repr__(self):
        return f"<Episode {self.name}>"
    
class EpisodesOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()