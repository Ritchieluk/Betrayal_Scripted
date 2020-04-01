from flask import Flask, request
import json, random, os.path
from os import path

app = Flask(__name__)
app.config["DEBUG"] = True

main_floor = [][]

for i in range(60):
    for j in range(60):
        main_floor[i][j] = 0



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
    if not path.exists('omens.json'):
        with open('omens.json', 'w') as outfile:
            json.dump(cards, outfile)
    for obj in cards:
        print('Card: {c}, GUID: {g}'.format(c=obj['nickname'], g=obj['guid']))
    chosen_card = random.choice(cards)
    print(chosen_card['guid'])
    return chosen_card['guid']

@app.route('/dealEvent', methods=['POST', 'PUT'])
def dealEvent():
    print(request.content_type)
    req = request.get_data()
    events = json.loads(req)
    print(events)
    print(len(events))
    if not path.exists('events.json'):
        with open('events.json', 'w') as outfile:
            json.dump(events, outfile)
    for obj in events:
        print('Card: {c}, GUID: {g}'.format(c=obj['nickname'], g=obj['guid']))
    chosen_card = random.choice(events)
    print(chosen_card['guid'])
    return chosen_card['guid']

@app.route('/dealItem', methods=['POST', 'PUT'])
def dealItem():
    print(request.content_type)
    req = request.get_data()
    items = json.loads(req)
    print(items)
    print(len(items))
    if not path.exists('items.json'):
        with open('items.json', 'w') as outfile:
            json.dump(items, outfile)
    for obj in items:
        print('Card: {c}, GUID: {g}'.format(c=obj['nickname'], g=obj['guid']))
    chosen_card = random.choice(items)
    print(chosen_card['guid'])
    return chosen_card['guid']

@app.route('/dealTile', methods=['POST', 'PUT'])
def dealTile():
    print(request.content_type)
    req = request.get_data()
    tiles = json.loads(req)
    print(tiles)
    print(len(tiles))
    if not path.exists('tiles.json'):
        with open('tiles.json', 'w') as outfile:
            json.dump(tiles, outfile)
    for obj in tiles:
        print('Card: {c}, GUID: {g}'.format(c=obj['nickname'], g=obj['guid']))
    chosen_card = random.choice(tiles)
    print(chosen_card['guid'])
    return chosen_card['guid']