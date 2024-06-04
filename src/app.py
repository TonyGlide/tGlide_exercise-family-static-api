import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_family_members():

    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_one_member_info(member_id):

    member_information = jackson_family.get_member(member_id)
    response_body = {
        "member": member_information
    }
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_one_member():

    request_body = request.get_json(force=True)
    jackson_family.add_member(request_body['first_name'],request_body['age'],request_body['lucky_numbers'])
    response_body = {
        "new member": "ok"
    }
    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_one_member(member_id):

    jackson_family.delete_member(member_id)
    response_body = {
        "member deleted": "done"
    }


    return jsonify(response_body), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)