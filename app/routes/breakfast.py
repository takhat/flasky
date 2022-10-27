#1. create a class about breakfast 
from flask import Blueprint, jsonify, request
from app import db


'''class Breakfast:
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
'''

breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")
from app.models.breakfast import Breakfast

@breakfast_bp.route('', methods=['GET'])
def get_all_breakfasts():
   
    result = []
    all_breakfasts = Breakfast.query.all()
    for item in all_breakfasts:
        item_dict = {"id": item.id, 
        "name": item.name,
        "rating":item.rating,
        "prep_time": item.prep_time}
        result.append(item_dict)
    return jsonify(result), 200
'''
@breakfast_bp.route('/<breakfast_id>', methods=['GET'])
def get_one_breakfast(breakfast_id):
    
    try:
        breakfast_id = int(breakfast_id)
    except ValueError:
        return jsonify({"msg": f"invalid data type: {breakfast_id}"}), 400
    chosen_breakfast = None
    all_breakfasts = Breakfast.query.all()
    for item in all_breakfasts:
        if item.id == breakfast_id:
            chosen_breakfast = item
    if chosen_breakfast is None:
        return({"msg": f"could not find breakfast item with id: {breakfast_id}"}), 404
    result = {
        'id': chosen_breakfast.id,
        "name": chosen_breakfast.name,
        "rating": chosen_breakfast.rating,
        "prep_time": chosen_breakfast.prep_time
    } 
    
    return jsonify(result), 200
'''
@breakfast_bp.route("",methods=["POST"])
def create_one_breakfast():
    request_body = request.get_json()
    new_breakfast = Breakfast(
        name = request_body["name"], 
        rating = request_body["rating"], 
        prep_time = request_body["prep_time"]
        )
    db.session.add(new_breakfast)
    db.session.commit()

    return jsonify(
        {"msg":f"successfully created breakfast with id: \
        {new_breakfast.id}"}, 201
        )

