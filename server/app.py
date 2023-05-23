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

    def post(self):
        try:
            data = request.get_json()
            team = Team(name=data['name'])
            db.session.add(team)
            db.session.commit()
            return {'message': 'Team created!', 'team': team.to_dict()}, 201
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

    def put(self, team_id):
        try:
            team = Team.query.get(team_id)
            if not team:
                return {'message': 'Team not found!'}, 404
            
            data = request.get_json()
            team.name = data['name']
            db.session.commit()
            
            return {'message': 'Team updated!', 'team': team.to_dict()}, 200
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

    def delete(self, team_id):
        try:
            team = Team.query.get(team_id)
            if not team:
                return {'message': 'Team not found!'}, 404
            
            db.session.delete(team)
            db.session.commit()
            
            return {'message': 'Team deleted!'}, 200
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

class Tournaments(Resource):
    def get(self):
        tournaments = Tournament.query.all()
        return [tournament.to_dict() for tournament in tournaments]

    def post(self):
        try:
            data = request.get_json()
            tournament = Tournament(name=data['name'], date=data['date'], location=data['location'])
            db.session.add(tournament)
            db.session.commit()
            return {'message': 'Tournament created!', 'tournament': tournament.to_dict()}, 201
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

    def put(self, tournament_id):
        try:
            tournament = Tournament.query.get(tournament_id)
            if not tournament:
                return {'message': 'Tournament not found!'}, 404
            
            data = request.get_json()
            tournament.name = data['name']
            tournament.date = data['date']
            tournament.location = data['location']
            db.session.commit()
            
            return {'message': 'Tournament updated!', 'tournament': tournament.to_dict()}, 200
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

    def delete(self, tournament_id):
        try:
            tournament = Tournament.query.get(tournament_id)
            if not tournament:
                return {'message': 'Tournament not found!'}, 404
            
            db.session.delete(tournament)
            db.session.commit()
            
            return {'message': 'Tournament deleted!'}, 200
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400
    

class Matches(Resource):
    def get(self):
        matches = Match.query.all()
        return [match.to_dict() for match in matches]

    def post(self):
        try:
            data = request.get_json()
            match = Match(team1=data['team1'], team2=data['team2'], date=data['date'], location=data['location'])
            db.session.add(match)
            db.session.commit()
            return {'message': 'Match created!', 'match': match.to_dict()}, 201
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

    def put(self, match_id):
        try:
            match = Match.query.get(match_id)
            if not match:
                return {'message': 'Match not found!'}, 404
            
            data = request.get_json()
            match.team1 = data['team1']
            match.team2 = data['team2']
            match.date = data['date']
            match.location = data['location']
            db.session.commit()
            
            return {'message': 'Match updated!', 'match': match.to_dict()}, 200
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

    def delete(self, match_id):
        try:
            match = Match.query.get(match_id)
            if not match:
                return {'message': 'Match not found!'}, 404
            
            db.session.delete(match)
            db.session.commit()
            
            return {'message': 'Match deleted!'}, 200
        except Exception as e:
            return {'message': 'Something went wrong!', 'error': str(e)}, 400

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