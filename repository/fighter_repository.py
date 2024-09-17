from dataclasses import asdict

from models.Fighter import Fighter
from repository.database import get_db_connection
from typing import List, Dict
from utils.json_loader import load_json


def load_fighters_from_json():
    all_fighters = find_all()
    if all_fighters and len(all_fighters) > 0:
        return
    fighters_json = load_json('../assets/data.json')
    for f in [Fighter(**f) for f in fighters_json]:
        create_fighter(f)

def create_fighter(fighter: Fighter) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO fighters (name, level, martial_art)
            VALUES (%s, %s, %s) RETURNING id
        """, (fighter.name, fighter.level, fighter.martial_art))
        new_id = cursor.fetchone()['id']
        connection.commit()
        return new_id


def find_all() -> List[Fighter]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fighters")
    res = cursor.fetchall()
    fighters = [Fighter(**f) for f in res]
    cursor.close()
    connection.close()
    return fighters