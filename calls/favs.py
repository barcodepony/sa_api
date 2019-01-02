from common.DBConnector import DBC
from flask import jsonify

global dbc
dbc = DBC()
dbc.connect()

def read_all():
    favs = []
    try:
        dbc.connect()
        favs = dbc.get_all_favs()
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(favs)


def read_one(f_id):
    fav = {}
    try:
        dbc.connect()
        fav = dbc.get_one_fav(f_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(fav)


def delete_one(f_id):
    try:
        dbc.connect()
        dbc.delete_one_fav(f_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()


def update_one(f_id, favourite):
    keys = ["f_category", "f_name", "f_poi", "f_label", "f_range"]
    for key in favourite:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    fav = {}
    fav["id"] = f_id
    fav["category"] = favourite["f_category"]
    fav["name"] = favourite["f_name"]
    fav["poi"] = favourite["f_poi"]
    fav["label"] = favourite["f_label"]
    fav["range"] = favourite["f_range"]
    print(fav)
    try:
        dbc.connect()
        dbc.update_one_fav(fav)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()


def create_one(favourite):
    keys = ["f_category", "f_name", "f_poi", "f_label", "f_range"]
    for key in favourite:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    fav = {}
    fav["category"] = favourite["f_category"]
    fav["name"] = favourite["f_name"]
    fav["poi"] = favourite["f_poi"]
    fav["label"] = favourite["f_label"]
    fav["range"] = favourite["f_range"]
    try:
        dbc.connect()
        dbc.insert_one_fav(fav)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
