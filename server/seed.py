from faker import Faker
from models import db, User, Team, Tournament, Match
from config import app


app.app_context().push()

fake = Faker()

def make_users(num_users):
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()
    

def make_teams(num_teams):
    for _ in range(num_teams):
        name = fake.word()

        team = Team(name=name)
        
    db.session.add(team)
    db.session.commit()

def make_tournaments(num_tournaments):
    for _ in range(num_tournaments):
        title = fake.sentence(nb_words=3)
        description = fake.paragraph()
        game_title = fake.word()

        tournament = Tournament(title=title, description=description, game_title=game_title)

    db.session.add(tournament)
    db.session.commit()

def make_matches(num_matches):
    teams = Team.query.all()
    tournaments = Tournament.query.all()

    for _ in range(num_matches):
        team1 = fake.random_element(teams)
        team2 = fake.random_element(teams)
        tournament = fake.random_element(tournaments)
        start_time = fake.date_time_this_year()
        end_time = start_time + fake.time_delta()

        match = Match(team1=team1, team2=team2, tournament=tournament, start_time=start_time, end_time=end_time)
        
    db.session.add(match)
    db.session.commit()

def make_all():
    num_users = 10
    num_teams = 5
    num_tournaments = 3
    num_matches = 5

    make_users(num_users)
    make_teams(num_teams)
    make_tournaments(num_tournaments)
    make_matches(num_matches)

    print("Seeding database...")

if __name__ == "__main__":
    make_all()