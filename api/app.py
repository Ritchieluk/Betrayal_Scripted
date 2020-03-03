from flask import Flask, request
import json, random

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>This is the API for a Betrayal Game</h1>"

@app.route('/dealOmen', methods=['POST', 'PUT'])
def dealOmen():
    print(request.content_type)
    req = request.get_data()
    cards = json.loads(req)
    print(cards)
    print(len(cards))
    for obj in cards:
        print('Card: {c}, GUID: {g}'.format(c=obj['nickname'], g=obj['guid']))
    chosen_card = random.choice(cards)
    print(chosen_card['guid'])
    return chosen_card['guid']