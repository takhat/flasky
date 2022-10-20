#1. create a class about breakfast 
from flask import Blueprint, jsonify

class Breakfast:
    def __init__(self, id, name, rating, prep_time):
        self.id = id
        self.name = name
        self.rating = rating
        self.prep_time = prep_time

breakfast_items = [
    Breakfast(1, "Pancakes", 4, 10),
    Breakfast(2, "Toast", 3, 15), 
    Breakfast(3, "Cereal", 1, 1), 
    Breakfast(4, "Oatmeal", 3, 10)
]

breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")


@breakfast_bp.route('', methods=['GET'])
def get_all_breakfasts():
    """converts a list of objects into a list of dictionaries"""
    result = []
    for item in breakfast_items:
        item_dict = {"id": item.id, 
        "name": item.name,
        "rating":item.rating,
        "prep_time": item.prep_time}
        result.append(item_dict)
    return jsonify(result), 200





