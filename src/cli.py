import click
from flask.cli import with_appcontext
from models import User, db

@click.command(name="createdb")
@with_appcontext
def create_db():
    db.create_all()
    db.session.commit()
    print("Database tables created")

@click.command(name="printdb")
@with_appcontext
def print_db():
    users = User.query.all()
    for user in users:
        print(user)

@click.command(name="cleardb")
@with_appcontext
def clear_db():
    db.drop_all()
    db.session.commit()
    print("Database tables cleared, remember to recreate them!")