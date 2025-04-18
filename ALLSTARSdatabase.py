from database import db

class AllStars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    nation = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Celebrity {self.name}>'