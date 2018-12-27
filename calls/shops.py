from common.DBConnector import DBC
from flask import jsonify
def read_all():
    dbc = DBC()
    dbc.connect()
    shops = dbc.get_all_shops()
    dbc.close_connection()
    return jsonify(shops)