from common.DBConnector import DBC
from flask import jsonify

def read_all():
    dbc = DBC()
    dbc.connect()
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


# TODO chgange to shops
def update_one(s_id, shop):
    keys = ["s_lon", "f_name", "f_poi", "f_label"]
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
