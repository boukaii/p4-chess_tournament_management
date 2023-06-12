from tinydb import TinyDB
from model import Tournament


def load_current_tournament():
    db = TinyDB("db.json", indent=4)
    table = db.table("current")
    if not table:
        return
    return Tournament.deserialize(table.all()[0])


def load_tournaments():
    db = TinyDB("db.json", indent=4)
    table = db.table("tournaments")
    if not table:
        return
    tournaments = []
    for data in table.all():
        tournaments.append(Tournament.deserialize(data))
    return tournaments


def load_players():
    tournaments = load_tournaments()
    if not tournaments:
        return []
    players = []
    for tournament in tournaments:
        players += tournament.players
    return str(players)
