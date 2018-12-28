from common.DBConnector import DBC
from flask import jsonify

def read_all():
    dbc = DBC()
    dbc.connect()
    shops = []
    try:
        shops = dbc.get_all_shops()
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(shops)

def read_one(s_id: int):
    dbc = DBC()
    shop = {}
    try:
        dbc.connect()
        shop = dbc.get_one_shop(s_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()
    return jsonify(shop)

def delete_one(s_id):
    dbc = DBC()
    try:
        dbc.connect()
        dbc.delete_one_shop(s_id)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()


# TODO chgange to shops
def update_one(s_id, shop):
    keys = ["s_lon", "s_lat", "s_name", "s_homepage", "s_category", "s_amenity"]
    for key in shop:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    dbc = DBC()
    s = {}
    s["id"] = s_id
    s["lon"] = shop["s_lon"]
    s["lat"] = shop["s_lat"]
    s["name"] = shop["s_name"]
    s["homepage"] = shop["s_homepage"]
    s["categorie"] = shop["s_category"]
    s["amenity"] = shop["s_amenity"]
    try:
        dbc.connect()
        dbc.update_one_shop(s)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()

def create_one(shop):
    keys = ["f_category", "f_name", "f_poi", "f_label"]
    for key in shop:
        if key in keys:
            keys.remove(key)
    if len(keys) > 0:
        print("ERROR: Not all keys within the request body (%s) .. aborting" % keys)
        return

    dbc = DBC()
    s = {}
    s["lon"] = shop["s_lon"]
    s["lat"] = shop["s_lat"]
    s["name"] = shop["s_name"]
    s["homepage"] = shop["s_homepage"]
    s["categorie"] = shop["s_category"]
    s["amenity"] = shop["s_amenity"]
    try:
        dbc.connect()
        dbc.insert_one_shop(s)
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()

def get_categories():

    dbc = DBC()
    category_dict = {}
    try:
        dbc.connect()
        category_dict = dbc.get_all_categories()
    except Exception as e:
        print("ERROR: %s" % e)
    finally:
        dbc.close_connection()

    return jsonify(category_dict)