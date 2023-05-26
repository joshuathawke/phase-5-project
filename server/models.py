from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash
from config import db




team_members = db.Table(
    'team_members',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True)
)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    avatar = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-created_at', '-updated_at')

    teams = db.relationship('Team', secondary=team_members, backref='members')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password_hash = generate_password_hash(password)
        self.avatar = None

    def __repr__(self):
        return f'<User {self.id} :: {self.username}>'



tournament_teams = db.Table(
    'tournament_teams',
    db.Column('tournament_id', db.Integer, db.ForeignKey('tournaments.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True)
)

class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    tournaments = db.relationship('Tournament', secondary=tournament_teams, backref='teams')

    serialize_rules = ('-created_at', '-updated_at')

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
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id"))
    team1_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team2_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    winner_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    team1 = db.relationship('Team', foreign_keys=[team1_id], backref='team1_matches')
    team2 = db.relationship('Team', foreign_keys=[team2_id], backref='team2_matches')

    serialize_rules = ('-created_at', '-updated_at')

    def __repr__(self):
        return f'<Match {self.id} :: Team 1: {self.team1_id}, Team 2: {self.team2_id}>'



