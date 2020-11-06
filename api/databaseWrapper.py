from simplemysql import simpleMysql

db = SimpleMysql(
    host="127.0.0.1",
    db="mydatabase",
    user="username",
    passwd="password",
    keep_alive=True
)


def buildTables():
    try:
        with open('sql/createDB.sql', 'r') as outfile:
            db.query(outfile)
        return True
    except Exception as e:
        print(e)
        return False

# ====== INSERT STATEMENTS =======

def insertTurn(gameID, playerID, turnNumber, numOmens, tilesFlipped, cardsDrawn):
    try:
        db.insert("turn_details", {turnNumber, numOmens, tilesFlipped, cardsDrawn})
        db.insert("turn_info", {db.lastID(), gameID, playerID})
        return True
    except Exception as e:
        print(e)
        return False

def addGame(date_played, num_players):
    try:
        db.insert("game_info", {date_played, num_players})
        return db.lastID()
    except Exception as e:
        print(e)
        return False

def addGameDetails(gameID, numTurns, gameRating, hauntNum):
    try:
        db.insert("game_details", {gameID, numTurns, gameRating, hauntNum})
        return db.lastID()
    except Exception as e:
        print(e)
        return False

def addPlayerInfo(gameID, characterName, playerPref):
    try:
        db.insert("player_info", {gameID, characterName, playerPref})
        return db.lastID()
    except Exception as e:
        print(e)
        return False

# ======= READ STATEMENTS ========

def getTurn(turnID):
    try:
        turn = db.getOne(
            "turn_details", 
            ["turnNumber", "numOmens", "tilesFlipped", "cardsDrawn"], 
            ("turnID={}".format(turnID))
        )
        turn.append(db.getOne(
            "turn_info",
            ["gameID", "playerID"],
            ("turnID={}".format(turnID))
        ))
        return turn
    except Exception as e:
        print(e)
        return False

def getAllTurnsByGame(gameID):
    try:
        turns = db.getAll(
            "turn_info",
            ["turnID", "playerID"],
            ("gameID={}".format(gameID))
        )
        for turn in turns:
            turn.append(db.getOne(
                "turn_details", 
                ["turnNumber", "numOmens", "tilesFlipped", "cardsDrawn"], 
                ("turnID={}".format(turnID))
            ))
        return turns
    except Exception as e:
        print(e)
        return False

def getAllTurnsByPlayer(gameID, playerID):
    try:
        turns = db.getAll(
            "turn_info",
            ["turnID", "playerID"],
            ("gameID={g}, playerID={p}".format(g=gameID, p=playerID))
        )
        for turn in turns:
            turn.append(db.getOne(
                "turn_details", 
                ["turnNumber", "numOmens", "tilesFlipped", "cardsDrawn"], 
                ("turnID={}".format(turnID))
            ))
        return turns
    except Exception as e:
        print(e)
        return False

def getPlayer(playerID):
     try:
        player = db.getOne(
            "player_info", 
            ["gameID", "characterName", "playerPref"], 
            ("playerID={}".format(playerID))
        )
        return player
    except Exception as e:
        print(e)
        return False

def getGame(gameID):
     try:
        game = db.getOne(
            "game_info", 
            ["date_played", "num_players"], 
            ("gameID={}".format(gameID))
        )
        game.append(db.getOne(
            "game_details",
            ["numTurns", "gameRating", "hauntNum"]
            ("gameID={}".format(gameID))
        ))
        return game
    except Exception as e:
        print(e)
        return False