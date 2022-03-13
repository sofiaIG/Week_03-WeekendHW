from flask import render_template, request
from app import app
from models.player import *
from models.game import *


@app.route('/game')
def index():
    return render_template("index.html", title = "Home") 

@app.route('/<choice_1>/<choice_2>', methods = ['POST'])
def add_choice(choice_1, choice_2):
    choice = request.form["choice"]
    choice_1 = Player(choice)
    game = Game()
    choice_2 = game.random_selection()
    return render_template("game_index.html", title = "game", game = game,
    choice_1 = choice_1,  choice_2 = choice_2 )

