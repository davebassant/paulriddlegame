from . import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)
    current_level = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.name}>'
