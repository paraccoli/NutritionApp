import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database.models import Base, Food, Meal
from database.db_connection import engine

def update_database():
    Base.metadata.bind = engine

    with engine.connect() as conn:
        try:
            # foods テーブルに category カラムを追加 (既に存在する場合はスキップ)
            conn.execute(text('ALTER TABLE foods ADD COLUMN category STRING'))
        except Exception as e:
            print(f"Error adding category column to foods table: {e}")
        
        try:
            # meals テーブルに meal_time カラムを追加
            conn.execute(text('ALTER TABLE meals ADD COLUMN meal_time STRING'))
            print("meal_time column added to meals table successfully.")
        except Exception as e:
            print(f"Error adding meal_time column to meals table: {e}")

        conn.commit()

    print("Database update process completed.")

if __name__ == "__main__":
    update_database()