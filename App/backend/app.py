import random
from experta import *
from random import choice
from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)


CORS(app)

global i
i = 0
global tab
tab = []


class Details(Fact):
    pass


# 0 means YES 1 mean NO


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Details(sport=0))
    def sport(self):
        global value
        value = ({"cadeau": "Bike"})
        tab.append(value)

    @Rule(Details(music=0))
    def music(self):
        global value
        value = ({"cadeau": "Piano"})
        tab.append(value)

    @Rule(Details(travel=0))
    def travel(self):
        global value
        value = ({"cadeau": "Going for a trip"})
        tab.append(value)

    @Rule(Details(reading=0))
    def reading(self):
        global value

        value = ({"cadeau": "Book"})
        tab.append(value)

    @Rule(Details(pets=0))
    def pets(self):
        global value
        value = ({"cadeau": "Buing a dog"})
        tab.append(value)

    @Rule(Details(videogames=0))
    def videogames(self):
        global value
        value = ({"cadeau": "CD of FiFa22"})
        tab.append(value)

    @Rule(Details(accessoires=0))
    def accessoires(self):
        global value
        value = ({"cadeau": "Buing a Mascara"})
        tab.append(value)

    @Rule(Details(drive=0))
    def drive(self):
        global value
        value = ({"cadeau": "Offer a car"})
        tab.append(value)

    @Rule(Details(clothes=0))
    def clothes(self):
        global value
        value = ({"cadeau": "Going for a shopping"})
        tab.append(value)

    @Rule(Details(all=1))
    def nothing(self):
        global value
        value = ({"cadeau": "Nothning to offer"})
        tab.append(value)


@app.route('/', methods=['GET'])
def get_response():
    tab.clear()


@app.route('/post', methods=['POST'])
def post_response():
    sport = request.json['sport']
    genre = request.json['genre']
    music = request.json['music']
    travel = request.json['travel']
    pets = request.json['pets']
    videogames = request.json['videogames']
    accessoires = request.json['accessoires']
    drive = request.json['drive']
    clothes = request.json['clothes']
    reading = request.json['reading']
    all = request.json['all']
    engine = RobotCrossStreet()
    engine.reset()
    engine.declare(
        Details(genre=genre, music=music, sport=sport, travel=travel,
                pets=pets, videogames=videogames, accessoires=accessoires, drive=drive, clothes=clothes,
                reading=reading, all=all))
    engine.run()
    i = (random.randint(0, len(tab)-1))
    print(tab)
    return (tab[i])


# if (__name__ == "__main__"):
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)