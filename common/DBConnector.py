import mysql.connector
from mysql.connector import Error
import logging
from common.SQL_CONSTANTS import *
from operator import itemgetter

class DBC(object):
    def __init__(self, host:str=GBL_HOST, port:int=GBL_PORT, db:str=GBL_DB, user:str=GBL_USER, password:str=GBL_PASSWORD):
        self.host = host
        self.port = port
        self.db = db
        self.__user = user
        self.__password = password
        self.connection = None
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      database=self.db,
                                                      port=self.port,
                                                      user=self.__user,
                                                      password=self.__password)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL database... MySQL Server version on ",db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print ("You are connected to - ", record)

        except Error as e:
            print("Error while connection to DB: ", e)

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            print("Disconnecting Database Connector")

    def __execute(self, SQL):
        if self.connection is None:
            raise ConnectionError("Connection is not set.")
        if not self.connection.is_connected():
            raise ConnectionError("You are not connected to the DB!")

        cursor = self.connection.cursor()
        print("CALLING: %s" % SQL)
        cursor.execute(SQL)
        rec = cursor.fetchall()
        return rec

    def get_all_shops(self):
        records = self.__execute(SELECT_SHOPS)

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

    def get_all_favs(self):
        records = self.__execute(SELECT_FAVS)
        # TODO: filter records

        favs = []
        for fav in records:

            f = {}
            f["f_id"] = fav[0]
            f["f_category"] = fav[1]
            f["f_name"] = fav[2]
            f["f_poi"] = fav[3]
            favs.append(f)

        favs.sort(key=itemgetter("f_id"))
        return favs

    def get_all_pois(self):
        records = self.__execute(SELECT_POIS)
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




if __name__ == "__main__":
    dbc = DBC()
    dbc.connect()
    dbc.get_all_favs()
    # rec = dbc.execute("select * from fav;")
    dbc.close_connection()