from common.DBConnector import DBC
from flask import jsonify
global dbc
dbc = DBC()
dbc.connect()

def read_all():
    try:
        dbc.connect()
        pois = dbc.get_all_pois()
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(pois)

def read_all_dict():
    try:
        dbc.connect()
        pois_dict = dbc.get_all_pois_as_dict()
        return pois_dict
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()



def read_one(p_id: int):
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

    p = {}
    p["id"] = p_id
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
    keys = ["p_lon", "p_lat", "p_name", "p_label"]
    for key in poi:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    p = {}
    p["lon"] = poi["p_lon"]
    p["lat"] = poi["p_lat"]
    p["name"] = poi["p_name"]
    p["amenity"] = poi["p_amenity"]
    try:
        dbc.connect()
        dbc.insert_one_poi(p)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
