from common.DBConnector import DBC
from flask import jsonify

def read_all():
    dbc = DBC()
    try:
        dbc.connect()
        favs = dbc.get_all_pois()
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(favs)


def read_one(p_id: int):
    dbc = DBC()
    poi = {}
    try:
        dbc.connect()
        poi = dbc.get_one_poi(p_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(poi)

def delete_one(p_id):
    dbc = DBC()
    try:
        dbc.connect()
        dbc.delete_one_poi(p_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()


def update_one(p_id, poi):
    keys = ["p_lon", "p_lat", "p_name", "p_amenity"]
    for key in poi:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    dbc = DBC()
    p = {}
    p["lon"] = poi["p_lon"]
    p["lat"] = poi["p_lat"]
    p["name"] = poi["p_name"]
    p["amenity"] = poi["p_amenity"]
    try:
        dbc.connect()
        dbc.update_one_poi(p)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()

def create_one(poi):
    return