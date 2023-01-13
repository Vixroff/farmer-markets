from model.mysql.connection import create_connection


GET_MARKETS_DATA = """
SELECT ma.idMarkets, ma.fmid, ma.marketname,
st.state, co.county, ci.city, zi.zip, lo.street, lo.x, lo.y,
me.youtube, me.facebook, me.website, me.othermedia,
se.season1, se.season1_time, se.season2, se.season2_time, se.season3, se.season3_time, se.season4, se.season4_time,
re.rate
FROM FarmMarkets.Markets as ma
	INNER JOIN FarmMarkets.Locations as lo ON ma.idMarkets = lo.Markets_idMarkets
		LEFT JOIN FarmMarkets.States as st ON lo.States_idStates = st.idStates
		LEFT JOIN FarmMarkets.Counties as co ON lo.Counties_idCounties = co.idCounties
		LEFT JOIN FarmMarkets.Cities as ci ON lo.Cities_idCities = ci.idCities
		LEFT JOIN FarmMarkets.Zips as zi ON lo.Zips_idZips = zi.idZips
	INNER JOIN FarmMarkets.Media as me ON ma.idMarkets = me.Markets_idMarkets
	INNER JOIN FarmMarkets.Seasons as se ON ma.idMarkets = se.Markets_idMarkets
	LEFT JOIN FarmMarkets.Reviews as re ON ma.idMarkets = re.Markets_idMarkets
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


def get_data():
    result = []
    status, answer = create_connection("FarmMarkets")
    if status is True:
        db = answer
        cursor = db.cursor(dictionary=True, buffered=True)
        cursor.execute(GET_MARKETS_DATA)
        markets = cursor.fetchall()
        for market in markets:
            cursor.execute(GET_MARKET_CATEGORIES, [market['idMarkets']])
            categories = cursor.fetchall()
            cursor.execute(GET_MARKET_PAYMENTS, [market['idMarkets']])
            payments = cursor.fetchall()
            market = market | categories[0] | payments[0]
            result.append(market)
        return result
    else:
        print(answer)


if __name__ == "__main__":
    result = get_data()
    print(result)
