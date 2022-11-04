from app import db

class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    rating = db.Column(db.Float)
    prep_time = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "prep_time": self.prep_time
        } 
    
    @classmethod
    def from_dict(cls, dict):
        return Breakfast(
            name = dict["name"],
            rating = dict["rating"],
            prep_time = dict["prep_time"]
        )

