from dataclasses import asdict

from flask import Blueprint, jsonify
from repository.fighter_repository import find_all

fighter_blueprint = Blueprint("fighter", __name__)

@fighter_blueprint.route("/", methods=['GET'])
def get_all():
    fighters = list(map(asdict, find_all()))
    return jsonify(fighters), 200


