from common.DBConnector import DBC
from flask import jsonify


def read_all():
    dbc = DBC()
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
    dbc = DBC()
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
    dbc = DBC()
    try:
        dbc.connect()
        dbc.delete_one_fav(f_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()


def update_one(f_id, favourite):
    keys = ["f_category", "f_name", "f_poi", "f_label"]
    for key in favourite:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    dbc = DBC()
    fav = {}
    fav["id"] = f_id
    fav["category"] = favourite["f_category"]
    fav["name"] = favourite["f_name"]
    fav["poi"] = favourite["f_poi"]
    fav["label"] = favourite["f_label"]
    try:
        dbc.connect()
        dbc.update_one_fav(fav)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()


def create_one(favourite):
    keys = ["f_category", "f_name", "f_poi", "f_label"]
    for key in favourite:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    dbc = DBC()
    fav = {}
    fav["category"] = favourite["f_category"]
    fav["name"] = favourite["f_name"]
    fav["poi"] = favourite["f_poi"]
    fav["label"] = favourite["f_label"]
    try:
        dbc.connect()
        dbc.insert_one_fav(fav)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
