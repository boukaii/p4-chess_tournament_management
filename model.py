from tinydb import TinyDB


class Player:
    def __init__(self, first_name, last_name, date_birth, gender, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.gender = gender
        self.score = score
        self.tournament = None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def serialize(self):
        data = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_birth": self.date_birth,
            "gender": self.gender,
            "score": self.score,
        }
        return data

    @classmethod
    def deserialize(cls, data):
        player = cls(data["last_name"], data["first_name"], data["date_birth"], data["gender"], data["score"])
        return player


class Tournament:
    def __init__(self, name, place, date, description, nb_tour=4, nb_players=8):
        self.name = name
        self.place = place
        self.date = date
        self.nb_tour = nb_tour
        self.rounds = []
        self.players = []
        self.description = description
        self.nb_players = nb_players

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round_):
        self.rounds.append(round_)
        return round_

    def serialize(self):
        data = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "description": self.description,
            "nb_tour": self.nb_tour,
            "players": [player.serialize() for player in self.players],
            "rounds": [round.serialize() for round in self.rounds],
            "nb_players": self.nb_players
        }
        return data

    @classmethod
    def deserialize(cls, data):
        tournament = cls(data['name'], data['place'], data['date'], data['description'], data['nb_tour'], data['nb_players'])
        for players_data in data["players"]:
            tournament.add_player(Player.deserialize(players_data))
        for rounds_data in data["rounds"]:
            tournament.add_round(Round.deserialize(rounds_data))
        return tournament

    def save(self, as_current=True):
        db = TinyDB("db.json", indent=4)
        table = db.table("current")
        table.truncate()
        if not as_current:
            table = db.table("tournaments")
        table.insert(self.serialize())


class Round:
    def __init__(self, name=None):
        self.name = name
        self.matchs = []

    def add_match(self, match):
        self.matchs.append(match)

    def serialize(self):
        data = {
            "name": self.name,
            "matchs": [s.serialize() for s in self.matchs]
        }
        return data

    @classmethod
    def deserialize(cls, data):
        round = cls(data["name"])
        for match_data in data["matchs"]:
            round.add_match(Match.deserialize(match_data))
        return round


class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def serialize(self):
        data = {
            "player1": self.player1.serialize(),
            "player2": self.player2.serialize(),
            "score_player1": self.score_player1,
            "score_player2": self.score_player2,
        }
        return data

    @classmethod
    def deserialize(cls, data):
        match = cls(data["player1"], data["player2"], data["score_player1"], data["score_player2"])
        return match
