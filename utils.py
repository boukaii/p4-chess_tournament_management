from tinydb import TinyDB
from model1 import Tournament


def load_current_tournament():
    db = TinyDB("db.json", indent=4)
    table = db.table("current")
    if not table:
        return
    return Tournament.deserialize(table.all()[0])
