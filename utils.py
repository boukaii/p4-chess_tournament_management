from tinydb import TinyDB, Query
from model import Tournament


def load_current_tournament():
    db = TinyDB("db.json", indent=4)
    table = db.table("current")
    # User = Query()
    # print(db.search(User.first_name))
    if not table:
        return
    return Tournament.deserialize(table.all()[0])
