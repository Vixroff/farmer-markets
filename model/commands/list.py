GET_MARKETS_DATA = """
SELECT idMarkets, fmid, marketname,
state, county, city, zip, street, x, y,
youtube, facebook, website, othermedia,
season1, season1_time, season2, season2_time, season3, season3_time, season4, season4_time
FROM FarmMarkets.Markets as ma
	INNER JOIN FarmMarkets.Locations as lo ON ma.idMarkets = lo.Markets_idMarkets
		LEFT JOIN FarmMarkets.States as st ON lo.States_idStates = st.idStates
		LEFT JOIN FarmMarkets.Counties as co ON lo.Counties_idCounties = co.idCounties
		LEFT JOIN FarmMarkets.Cities as ci ON lo.Cities_idCities = ci.idCities
		LEFT JOIN FarmMarkets.Zips as zi ON lo.Zips_idZips = zi.idZips
	INNER JOIN FarmMarkets.Media as me ON ma.idMarkets = me.Markets_idMarkets
	INNER JOIN FarmMarkets.Seasons as se ON ma.idMarkets = se.Markets_idMarkets
"""


GET_MARKET_PAYMENTS = """
SELECT GROUP_CONCAT(pa.payment) AS payments
FROM FarmMarkets.Markets AS ma
	INNER JOIN FarmMarkets.Markets_has_Payments AS mhp
		ON ma.idMarkets = mhp.Markets_idMarkets
	INNER JOIN FarmMarkets.Payments as pa
		ON mhp.Payments_idPayments = pa.idPayments
WHERE ma.idMarkets = %s
"""


GET_MARKET_CATEGORIES = """
SELECT GROUP_CONCAT(ca.category) as categories
FROM FarmMarkets.Markets AS ma
	INNER JOIN FarmMarkets.Markets_has_Categories AS mhc
		ON ma.idMarkets = mhc.Markets_idMarkets
	INNER JOIN FarmMarkets.Categories as ca
		ON mhc.Categories_idCategories = ca.idCategories
WHERE ma.idMarkets = %s
"""


GET_RATING = """
SELECT ROUND(AVG(IFNULL(re.rate, 0)), 2) AS rate
FROM FarmMarkets.Markets AS ma
	LEFT JOIN FarmMarkets.Reviews AS re
		ON ma.idMarkets = re.Markets_idMarkets
WHERE ma.idMarkets = %s
"""


def get_data(cursor):
	result = []
	cursor.execute(GET_MARKETS_DATA)
	markets = cursor.fetchall()
	for market in markets:
		cursor.execute(GET_MARKET_CATEGORIES, [market['idMarkets']])
		categories = cursor.fetchall()[0]
		cursor.execute(GET_MARKET_PAYMENTS, [market['idMarkets']])
		payments = cursor.fetchall()[0]
		cursor.execute(GET_RATING, [market['idMarkets']])
		rating = cursor.fetchall()[0]
		market = market | categories | payments | rating
		result.append(market)
	return result


if __name__ == "__main__":
    result = get_data()
    for row in result:
        print(row)
        print('\n')
