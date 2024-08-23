from flask import Flask, request, jsonify
from services import meal_service, user_service, goal_service
from database.models import User
from database.db_connection import get_db

app = Flask(__name__)

@app.route('/api/sync/meals', methods=['POST'])
def sync_meals():
    user_id = request.json['user_id']
    meals = request.json['meals']
    for meal in meals:
        meal_service.add_meal(user_id, meal['food_name'], meal['amount'])
    return jsonify({"status": "success"})

@app.route('/api/sync/profile', methods=['POST'])
def sync_profile():
    user_id = request.json['user_id']
    profile_data = request.json['profile']
    user_service.update_user_profile(user_id, profile_data)
    return jsonify({"status": "success"})

@app.route('/api/sync/goals', methods=['POST'])
def sync_goals():
    user_id = request.json['user_id']
    goals = request.json['goals']
    for goal in goals:
        goal_service.set_goal(user_id, goal['goal_type'], goal['target_value'], goal['target_date'])
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
