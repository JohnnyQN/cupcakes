from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake model with predefined size categories."""

    __tablename__ = "cupcakes"

    SIZE_CHOICES = ['small', 'medium', 'large']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(Enum(*SIZE_CHOICES, name="cupcake_size"), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE)

    def serialize_cupcake(self):
        """Return serialized cupcake info."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }
