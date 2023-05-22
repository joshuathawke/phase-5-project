from flask import request, jsonify
from app import app, db
from models import User, Team, Tournament, Match



@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify(user)





