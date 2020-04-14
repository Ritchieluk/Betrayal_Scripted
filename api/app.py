from flask import Flask, request
import json, random, os.path
from os import path

app = Flask(__name__)
app.config["DEBUG"] = True

layout = {'entrance': [], 'basement': [], 'upper': [], 'roof': []}
ids = {}
tiles = []
with open('ids.json', 'r') as outfile:
    ids = json.load(outfile)
with open('tiles.json', 'r') as outfile:
    tiles = json.load(outfile)

object_locations = {}

tiles_in_use = []

for key in layout.keys():
    for i in range(60):
        row = []
        for j in range(60):
            if i == 30 and j == 30:
                row.append(ids[key])
            else:
                row.append(0)
        layout[key].append(row)



@app.route('/', methods=['GET'])
def home():
    return "<h1>This is the API for a Betrayal Game</h1>"

@app.route('/dealOmen', methods=['POST', 'PUT'])
def dealOmen():
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

@app.route('/dealTileMaster', methods=['POST', 'GET', 'PUT'])
def dealTileMaster():
    if len(tiles) == 0:
        return json.dumps({'response': 'False'})
    index = 0
    while(tiles[index]['guid'] in tiles_in_use):
        index = random.choice(range(len(tiles)))
    else:
        chosen_card = tiles[index]
        tiles_in_use.append(tiles.pop(index)['guid'])
        return json.dumps(chosen_card)

@app.route('/createJSONObject', methods=['PUT'])
def createJSON():
    objs = json.loads(request.get_data())
    print(objs)
    file_path = str(objs['Nickname'])+'.json'
    if not path.exists(file_path):
        with open(file_path, 'w') as outfile:
                json.dump(objs, outfile)
    return "JSONs created"


@app.route('/updateObjectLocation', methods=['PUT'])
def updateObjectLocation():
    obj = json.loads(request.get_data())
    if(obj['GUID'] in object_locations.keys()):
        print('Object {} moved'.format(obj['GUID']))
    object_locations[obj['GUID']] = obj['Transform']
    return obj