from common.LOCK import LOCK_HOST, LOCK_PASSWORD

GBL_HOST = LOCK_HOST
GBL_PORT = 3306
GBL_DB = "SA"
GBL_USER = "sa"
GBL_PASSWORD = LOCK_PASSWORD

SELECT_ALL_FAVS = "SELECT * FROM fav;"
SELECT_ONE_FAV = "SELECT * FROM fav where id = %s;"
UPDATE_FAV_BY_ID = "UPDATE fav SET category='%s', name='%s', poi='%s', label='%s', `range`=%s where id = %s;"
DELETE_FAV_BY_ID = "DELETE FROM fav WHERE id = %s;"
INSERT_ONE_FAV = "INSERT INTO fav (category, name, poi, label, range) VALUES ('%s', '%s', '%s', '%s', '%s');"




SELECT_ALL_SHOPS = "SELECT * FROM shops;"
SELECT_ONE_SHOP = "SELECT * FROM shops where id = %s"
UPDATE_SHOP_BY_ID = "UPDATE shops SET lon='%s', lat='%s', name='%s', homepage='%s', categorie='%s', amenity='%s' where id=%s;"
DELETE_SHOP_BY_ID = "DELETE FROM shops WHERE id = %s;"
INSERT_ONE_SHOP = "INSERT INTO shops (lon, lat, name, homepage, categorie, amenity) VALUES (%s,%s,'%s','%s','%s','%s');"
SELECT_ALL_CATEGORIES = "select categorie from shops group by categorie;"
SELECT_FILTERED_SHOPS = "SELECT * FROM shops WHERE %s;"

SELECT_ALL_POIS = "SELECT * FROM poi where name <> '';"
SELECT_ONE_POI = "SELECT * FROM poi where id = %s;"
UPDATE_POI_BY_ID = "UPDATE poi SET lon='%s', lat='%s', name='%s', amenity='%s' where id=%s;"
DELETE_POI_BY_ID = "DELETE FROM poi WHERE id = %s;"
INSERT_ONE_POI = "INSERT INTO poi (lon, lat, name, amenity) VALUES (%s, %s, '%s', '%s' );"

# https://stackoverflow.com/questions/1006654/fastest-way-to-find-distance-between-two-lat-long-points
