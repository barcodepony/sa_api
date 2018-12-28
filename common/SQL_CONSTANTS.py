from common.LOCK import LOCK_HOST, LOCK_PASSWORD

GBL_HOST = LOCK_HOST
GBL_PORT = 3306
GBL_DB = "SA"
GBL_USER = "sa"
GBL_PASSWORD = LOCK_PASSWORD

SELECT_ALL_FAVS = "SELECT * FROM fav;"
SELECT_ONE_FAV = "SELECT * FROM fav where id = %s;"
UPDATE_FAV_BY_ID = "UPDATE fav SET category='%s', name='%s', poi='%s', label='%s' where id = %s;"
DELETE_FAV_BY_ID = "DELETE FROM fav WHERE id = %s;"
INSERT_ONE_FAV = "INSERT INTO fav (category, name, poi, label) VALUES ('%s', '%s', '%s', '%s');"



SELECT_ALL_SHOPS = "SELECT * FROM shops;"
SELECT_ONE_SHOP = "SELECT * FROM shops where id = %s"
UPDATE_SHOP_BY_ID = "UPDATE shop SET lon='%s', lat='%s', name='%s', homepage='%s', categorie='%s', amenity='%s' where id=%s;"
DELETE_SHOP_BY_ID = "DELETE FROM shops WHERE id = %s;"
INSERT_ONE_SHOP = "INSERT INTO shop (lon, lat, name, homepage, categorie, amenity) VALUES (%s,%s,'%s','%s','%s','%s',);"
SELECT_ALL_CATEGORIES = "select categorie from shops group by categorie;"

SELECT_ALL_POIS = "SELECT * FROM poi;"
SELECT_ONE_POI = "SELECT * FROM poi where id = %s;"
UPDATE_POI_BY_ID = "UPDATE poi SET lon='%s', lat='%s', name='%s', amenity='%s' where id=%s;"
DELETE_POI_BY_ID = "DELETE FROM poi WHERE id = %s;"
INSER_ONE_POI = "INSERT INTO poi (lon, lat, name, amenity) VALUES (%s, %s, '%s', '%s' );"
