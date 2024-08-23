from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.db_connection import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    meals = relationship("Meal", back_populates="user")
    profile = relationship("UserProfile", uselist=False, back_populates="user")
    goals = relationship("Goal", back_populates="user")

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    name = Column(String)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    user = relationship("User", back_populates="profile")

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    category = Column(String)

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    meal_time = Column(String)  # 'breakfast', 'lunch', or 'dinner'

    user = relationship("User", back_populates="meals")
    food = relationship("Food")

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    goal_type = Column(String)  # e.g., "weight_loss", "calorie_intake", "protein_intake"
    target_value = Column(Float)
    current_value = Column(Float)
    target_date = Column(DateTime)
    achieved = Column(Boolean, default=False)

    user = relationship("User", back_populates="goals")