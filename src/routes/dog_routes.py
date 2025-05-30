from flask import Blueprint, jsonify
from src.usecases.dog_usecase import DogUseCase

dog_blueprint = Blueprint('dog_routes', __name__)
usecase = DogUseCase()

@dog_blueprint.route('/breeds', methods=['GET'])
def get_breeds():
    return jsonify(usecase.get_breeds())

@dog_blueprint.route('/breeds/<breed_id>', methods=['GET'])
def get_breed(breed_id):
    return jsonify(usecase.get_breed(breed_id))

@dog_blueprint.route('/facts', methods=['GET'])
def get_facts():
    return jsonify(usecase.get_facts())

@dog_blueprint.route('/groups', methods=['GET'])
def get_groups():
    return jsonify(usecase.get_groups())

@dog_blueprint.route('/groups/<group_id>', methods=['GET'])
def get_group(group_id):
    return jsonify(usecase.get_group(group_id))

@dog_blueprint.route('/group-details/<group_id>', methods=['GET'])
def get_group_details(group_id):
    return jsonify(usecase.get_group_details(group_id))

@dog_blueprint.route('/group-details/<group_id>/breed/<breed_id>', methods=['GET'])
def get_group_breed(group_id, breed_id):
    return jsonify(usecase.get_group_breed(group_id, breed_id))
