import pytest

from models.Fighter import Fighter
from repository.database import create_tables, get_db_connection
from repository.fighter_repository import create_fighter, find_all, load_fighters_from_json, count_things
from operator import  eq

@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    load_fighters_from_json()
    yield
    # tear down - happens after test finished
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE fighters")
    connection.commit()
    cursor.close()
    connection.close()

