from database.models import User, UserProfile
from database.db_connection import get_db
from sqlalchemy.orm import Session

def get_user_profile(user_id: int):
    db = next(get_db())
    try:
        return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    finally:
        db.close()

def update_user_profile(user_id: int, profile_data: dict):
    db: Session = next(get_db())
    try:
        profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        if profile:
            for key, value in profile_data.items():
                setattr(profile, key, value)
        else:
            profile = UserProfile(user_id=user_id, **profile_data)
            db.add(profile)
        
        db.commit()
        db.refresh(profile)
        return profile
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()