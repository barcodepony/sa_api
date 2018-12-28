from common.LOCK import LOCK_HOST, LOCK_PASSWORD

GBL_HOST = LOCK_HOST
GBL_PORT = 3306
GBL_DB = "SA"
GBL_USER = "sa"
GBL_PASSWORD = LOCK_PASSWORD


SELECT_FAVS = "SELECT * FROM fav;"
SELECT_ONE_FAV = "SELECT * FROM fav where id = %s;"
UPDATE_FAV_BY_ID = "UPDATE fav SET category='%s', name='%s', poi='%s', label='%s' where id = %s;"

SELECT_SHOPS = "SELECT * FROM shops;"
SELECT_ONE_SHOP = "SELECT * FROM shops where id = %s"
UPDATE_SHOP_BY_ID = "UPDATE shop SET lon='%s', lat='%s', name='%s', homepage='%s', categorie='%s', amenity='%s' where id=%s;"

SELECT_POIS = "SELECT * FROM poi;"
SELECT_ONE_POI = "SELECT * FROM poi where id = %s;"
UPDATE_POI_BY_ID = "UPDATE poi SET lon='%s', lat='%s', name='%s', amenity='%s' where id=%s;"
