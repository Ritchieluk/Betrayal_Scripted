CREATE TABLE game_info (gameID AUTO_INCREMENT, date_played datetime, num_players int, PRIMARY KEY (gameID));

CREATE TABLE player_info (playerID AUTO_INCREMENT, gameID int, characterName int, playerPref json, PRIMARY KEY (playerID));

CREATE TABLE game_details (gameDetailsID AUTO_INCREMENT, gameID int, numTurns int, gameRating float, hauntNum int, PRIMARY KEY (gameDetailsID));

CREATE TABLE turn_details (turnID AUTO_INCREMENT, turnNumber int, numOmens int, tilesFlipped json, cardsDrawn json, PRIMARY KEY (turnID));

CREATE TABLE turn_info (turnID int, gameID int, playerID int);