from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_name = db.Column(db.String)
    meal =db.Column(db.String)
    breakfast_items= db.relationship("Breakfast", back_populates="menu")
    
    def to_dict(self):
        list_of_breakfasts = []
        for item in self.breakfast_items:
            list_of_breakfasts.append(item.to_dict())
        return {
            "id": self.id,
            "restaurant_name": self.restaurant_name,
            "meal": self.meal,
            "breakfast_items": list_of_breakfasts
        } 
    @classmethod
    def get_breakfast_list(cls):
        breakfasts = []
        for item in cls.breakfast_items:
            breakfasts.append(item.to_dict())
        return (breakfasts)
