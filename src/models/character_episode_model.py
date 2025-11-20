from src.models import db

class characterEpisode(db.Model):
    __tablename__ = 'character_episode'
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)