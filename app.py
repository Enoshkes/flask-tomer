from flask import Flask
from controllers.fighter_controller import fighter_blueprint
from repository.database import create_tables
from repository.fighter_repository import load_fighters_from_json

app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    load_fighters_from_json()
    app.register_blueprint(fighter_blueprint, url_prefix="/api/fighters")
    app.run(debug=True)