from flask import request, session, make_response
from flask_restful import Resource
from config import app, db, api
from models import User, Team, Tournament, Match

class Home(Resource):
    def get(self):
        return make_response({'message': 'Hello World!'}, 202)

class Signup(Resource):
    def post(self):
        try:
            new_user = User(username=request.get_json()['username'], email=request.get_json()['email'], password=request.get_json()['password'])
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return make_response({'message': 'Account Created!', 'user': new_user.id}, 201)
        except Exception as e:
            return make_response({'message': 'Something went wrong!', 'stackTrace': str(e)}, 400)

class Login(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.verify_password(password):
            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):
    def get(self):
        session.pop('user_id', None)
        return make_response({'message': 'You logged out!'}, 200)

class DeleteAccount(Resource):
    def delete(self):
        try:
            user_id = session.get('user_id')
            if user_id:
                user = User.query.get(user_id)
                if user:
                    db.session.delete(user)
                    db.session.commit()
                    session.pop('user_id', None)
                    return make_response({'message': 'Account deleted!'}, 200)
            return make_response({'message': 'User not found!'}, 404)
        except Exception as e:
            return make_response({'message': 'Something went wrong!', 'stackTrace': str(e)}, 400)


class Teams(Resource):
    def get(self):
        teams = Team.query.all()
        return [team.to_dict() for team in teams]

class Tournaments(Resource):
    def get(self):
        tournaments = Tournament.query.all()
        return [tournament.to_dict() for tournament in tournaments]
    
class Matches(Resource):
    def get(self):
        matches = Match.query.all()
        return [match.to_dict() for match in matches]

api.add_resource(Home, '/')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(DeleteAccount, '/delete_account')
api.add_resource(Teams, '/teams')
api.add_resource(Tournaments, '/tournaments')
api.add_resource(Matches, '/matches')



if __name__ == '__main__':
    app.run(port=5555, debug=True)