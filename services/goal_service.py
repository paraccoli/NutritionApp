from database.models import Goal, User
from database.db_connection import get_db
from datetime import datetime

def set_goal(user_id: int, goal_type: str, target_value: float, target_date: datetime):
    db = next(get_db())
    new_goal = Goal(user_id=user_id, goal_type=goal_type, target_value=target_value, target_date=target_date)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

def get_user_goals(user_id: int):
    db = next(get_db())
    return db.query(Goal).filter(Goal.user_id == user_id).all()

def update_goal_progress(goal_id: int, current_value: float):
    db = next(get_db())
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if goal:
        goal.current_value = current_value
        db.commit()
        return True
    return False

def check_goal_achievement(user_id: int):
    db = next(get_db())
    goals = db.query(Goal).filter(Goal.user_id == user_id, Goal.achieved == False).all()
    for goal in goals:
        if goal.current_value >= goal.target_value:
            goal.achieved = True
            db.commit()
    return db.query(Goal).filter(Goal.user_id == user_id, Goal.achieved == True).all()