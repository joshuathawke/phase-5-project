from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy(metadata=MetaData())

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    avatar = db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default= db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-created_at','-updated_at' )

    teams = db.relationship('Team', secondary='team_members', backref='members')
   
    def __repr__(self):
        return f'<User {self.id} :: {self.username}>'

class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    created_at=db.Column(db.DateTime, server_default= db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    tournaments = db.relationship('Tournament', secondary='tournament_teams', backref='teams')

    serialize_rules = ('-created_at','-updated_at' )

    def __repr__(self):
        return f'<Team {self.id} :: {self.name}>'
   
class Tournament(db.Model, SerializerMixin):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    game_title = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at=db.Column(db.DateTime, server_default= db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    matches = db.relationship('Match', backref='tournament')

    serialize_rules = ('-created_at','-updated_at' )

    def __repr__(self):
        return f'<Tournament {self.id} :: {self.title}>'
   
class Match(db.Model, SerializerMixin):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    winner_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    created_at=db.Column(db.DateTime, server_default= db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-created_at','-updated_at' )

    def __repr__(self):
        return f'<Match {self.id} :: Team 1: {self.team1_id}, Team 2: {self.team2_id}>'
