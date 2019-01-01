from common.DBConnector import DBC
from flask import jsonify

def read_all(range, name=None, category=None, poi=None):
    # get all parameters and enable_states
    filter = {
        "name": False if name is None else True,
        "category": False if category is None else True,
        "poi": False if poi is None else True
    }

    fvalue = {
        "name": name,
        "category": category,
        "poi": poi,
        "range": range
    }

    filtered = False
    for key in filter:
        if filter[key]:
            filtered = True
            break
    dbc = DBC()
    dbc.connect()
    shops = []

    try:
        if filtered:
            shops = dbc.get_filtered_shops(filters=filter, values=fvalue)
        else:
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
    keys = ["s_lon", "s_lat", "s_name", "s_homepage", "s_category", "s_amenity"]
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
