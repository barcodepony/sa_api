import mysql.connector
from mysql.connector import Error
from common.SQL_CONSTANTS import *
from operator import itemgetter
import collections
from common.QueueClient import QueueClient

class DBC(object):
    def __init__(self, host:str = GBL_HOST, port: int = GBL_PORT, db: str = GBL_DB, user: str = GBL_USER, password: str = GBL_PASSWORD):
        self.host = host
        self.port = port
        self.db = db
        self.__user = user
        self.__password = password
        self.connection = None

    def connect(self):
        try:
            if isinstance(self.connection, mysql.connector.CMySQLConnection):
                if self.connection.is_connected():
                    print("reusing connection to SA")
                    return

            print("Building connection to SA")
            self.connection = mysql.connector.connect(host=self.host,
                                                      database=self.db,
                                                      port=self.port,
                                                      user=self.__user,
                                                      password=self.__password)
            if self.connection.is_connected():
                print("You are connected to SA")

        except Error as e:
            print("Error while connection to DB: ", e)

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            print("Disconnecting Database Connector")

    def __query_sql(self, sql):
        if self.connection is None:
            raise ConnectionError("Connection is not set.")
        if not self.connection.is_connected():
            raise ConnectionError("You are not connected to the DB!")

        cursor = self.connection.cursor()
        print("CALLING: %s" % sql)
        cursor.execute(sql)
        rec = cursor.fetchall()
        return rec
    def __execute_sql(self, sql, send_to_queue: bool=True):
        if send_to_queue:
            client = QueueClient()
            client.send(sql)
        elif not send_to_queue:
            if self.connection is None:
                raise ConnectionError("Connection is not set.")
            if not self.connection.is_connected():
                raise ConnectionError("You are not connected to the DB!")
            cursor = self.connection.cursor()
            print("EXECUTING: %s" % sql)
            cursor.execute(sql)
            self.connection.commit()

    def get_all_shops(self):
        records = self.__query_sql(SELECT_ALL_SHOPS)

        shops = []
        for shop in records:
            s = {}
            s["s_id"] = shop[0]
            s["s_lon"] = shop[1]
            s["s_lat"] = shop[2]
            s["s_name"] = shop[3]
            s["s_homepage"] = shop[4]
            s["s_category"] = shop[5]
            s["s_amenity"] = shop[6]
            shops.append(s)

        shops.sort(key=itemgetter("s_id"))
        return shops

    def get_filtered_shops(self, filters: dict, values: dict):

        condition_exists = False
        condition = ""

        if filters["category"]:
            if condition_exists:
                condition += " AND "
            condition_exists = True
            condition += "categorie='"+values["category"]+"'"

        if filters["poi"]:
            assert isinstance(values["poi"], int), "PoI needs to type of integer"
            assert isinstance(values["range"], int), "Range needs to be set, if a PoI is used"

            poi = self.get_one_poi(values["poi"])
            assert len(poi) > 0, "Invalid PoI return .. is there no ID %s?" % filters["poi"]
            lat = poi["p_lat"]
            lon = poi["p_lon"]



            if condition_exists:
                condition += " AND "
            condition_exists = True
            condition += "st_distance_sphere(POINT(lon, lat), Point(%s, %s)) < %s" % (lon, lat, values["range"])

        if filters["name"]:
            if condition_exists:
                condition += " AND "
            condition_exists = True
            condition += "name LIKE '%"+values["name"]+"%'"

        if condition == "":
            raise ValueError("The Condition is empty, after filter mogrify")


        records = self.__query_sql(SELECT_FILTERED_SHOPS % condition)

        shops = []
        for shop in records:
            s = {}
            s["s_id"] = shop[0]
            s["s_lon"] = shop[1]
            s["s_lat"] = shop[2]
            s["s_name"] = shop[3]
            s["s_homepage"] = shop[4]
            s["s_category"] = shop[5]
            s["s_amenity"] = shop[6]
            shops.append(s)

        shops.sort(key=itemgetter("s_id"))
        return shops

    def get_one_shop(self, s_id: int):
        record = self.__query_sql(SELECT_ONE_SHOP % s_id)
        if len(record) == 0:
            return {}
        else:
            record = record[0]

        s = {}
        s["s_id"] = record[0]
        s["s_lon"] = record[1]
        s["s_lat"] = record[2]
        s["s_name"] = record[3]
        s["s_homepage"] = record[4]
        s["s_category"] = record[5]
        s["s_amenity"] = record[6]
        return s

    def get_all_favs(self):
        records = self.__query_sql(SELECT_ALL_FAVS)
        favs = []
        for fav in records:

            f = {}
            f["f_id"] = fav[0]
            f["f_category"] = fav[1]
            f["f_name"] = fav[2]
            f["f_poi"] = fav[3]
            f["f_label"] = fav[4]
            f["f_range"] = fav[5]
            favs.append(f)

        favs.sort(key=itemgetter("f_id"))
        return favs

    def get_one_fav(self, f_id: int):
        record = self.__query_sql(SELECT_ONE_FAV % f_id)
        if len(record) == 0:
            return {}
        else:
            record = record[0]
        fav = {}
        fav["f_id"] = record[0]
        fav["f_category"] = record[1]
        fav["f_name"] = record[2]
        fav["f_poi"] = record[3]
        fav["f_label"] = record[4]
        fav["f_label"] = record[5]
        return fav

    def update_one_fav(self, favourite: dict):

        sql = UPDATE_FAV_BY_ID % (favourite["category"],
                                  favourite["name"],
                                  favourite["poi"],
                                  favourite["label"],
                                  favourite["range"],
                                  favourite["id"])
        self.__execute_sql(sql)

    def update_one_poi(self, poi: dict):
        sql = UPDATE_POI_BY_ID % (poi["lon"],
                                  poi["lat"],
                                  poi["name"],
                                  poi["amenity"],
                                  poi["id"])

        self.__execute_sql(sql)

    def update_one_shop(self, shop: dict):
        sql = UPDATE_SHOP_BY_ID % (shop["lon"],
                                   shop["lat"],
                                   shop["name"],
                                   shop["homepage"],
                                   shop["categorie"],
                                   shop["amenity"],
                                   shop["id"])
        self.__execute_sql(sql)

    def insert_one_fav(self, fav):
        sql = INSERT_ONE_FAV % (fav["category"],
                                fav["name"],
                                fav["poi"],
                                fav["label"],
                                fav["range"])

        self.__execute_sql(sql)

    def insert_one_shop(self, shop):
        sql = INSERT_ONE_SHOP % (shop["lon"],
                                 shop["lat"],
                                 shop["name"],
                                 shop["homepage"],
                                 shop["categorie"],
                                 shop["amenity"])

        self.__execute_sql(sql)

    def insert_one_poi(self, poi):
        sql = INSERT_ONE_POI % (poi["lon"],
                                poi["lat"],
                                poi["name"],
                                poi["amenity"])

        self.__execute_sql(sql)

    def get_all_categories(self):
        sql = SELECT_ALL_CATEGORIES
        records = self.__query_sql(sql)
        if len(records) == 0:
            return {}
        else:
            records = [cat[0] for cat in records]

        categories = {}
        for index, cat in enumerate(records):
            categories[index] = cat

        sorted_categories = collections.OrderedDict(sorted(categories.items()))

        return sorted_categories

    def delete_one_fav(self, f_id: int):
        sql = DELETE_FAV_BY_ID % f_id
        self.__execute_sql(sql)

    def delete_one_shop(self, s_id: int):
        sql = DELETE_SHOP_BY_ID % s_id
        self.__execute_sql(sql)

    def delete_one_poi(self, p_id: int):
        sql = DELETE_POI_BY_ID % p_id
        self.__execute_sql(sql)

    def get_all_pois(self):
        records = self.__query_sql(SELECT_ALL_POIS)
        # TODO: filter records

        pois = []
        for poi in records:
            p = {}
            p["p_id"] = poi[0]
            p["p_lon"] = poi[1]
            p["p_lat"] = poi[2]
            p["p_name"] = poi[3]
            p["p_amenity"] = poi[4]
            pois.append(p)

        pois.sort(key=itemgetter("p_id"))
        return pois

    def get_all_pois_as_dict(self):
        pois = self.get_all_pois()
        poi_dict = dict()
        for poi in pois:
            poi_dict[str(poi["p_id"])] = poi["p_name"]

        return poi_dict

    def get_one_poi(self, p_id: int):
        record = self.__query_sql(SELECT_ONE_POI % p_id)
        if len(record) == 0:
            return {}
        else:
            record = record[0]

        p = {}
        p["p_id"] = record[0]
        p["p_lon"] = record[1]
        p["p_lat"] = record[2]
        p["p_name"] = record[3]
        p["p_amenity"] = record[4]
        return p

    def __get_filter_count(self, filters:dict):
        count = 0
        for key in filters:
            count = count+1 if filters[key] is True else count


if __name__ == "__main__":
    dbc = DBC()
    dbc.connect()
    a = dbc.get_one_poi(-1)

    filter = {
        "name": True,
        "category": True,
        "poi": True
    }

    fvalue = {
        "name": "auer",
        "category": "bakery",
        "poi": 251710890,
        "range": 1000
    }

    b = dbc.get_filtered_shops(filters=filter, values=fvalue)
    c = dbc.get_all_pois_as_dict()

    # rec = dbc.execute("select * from fav;")
    dbc.close_connection()