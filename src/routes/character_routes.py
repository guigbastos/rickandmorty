from flask import Blueprint, request
from src.controllers.character_controller import CharacterController

character_bp = Blueprint('character_bp', __name__)
character_controller = CharacterController()

@character_bp.route('/', methods=['GET'])
def get_all_characters():
    # name = request.args.get('name', None)
    # return character_controller.get_all_characters(name)
    params = request.args.to_dict()
    return character_controller.get_all_characters(params)


@character_bp.route('/<int:id>', methods=['GET'])
def get_character_by_id(id):
    return character_controller.get_character_by_id(id)