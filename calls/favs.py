from common.DBConnector import DBC
from flask import jsonify

def read_all():
    dbc = DBC()
    dbc.connect()
    favs = dbc.get_all_favs()
    dbc.close_connection()
    return jsonify(favs)