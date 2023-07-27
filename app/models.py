from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Cocktail {self.name}>"
