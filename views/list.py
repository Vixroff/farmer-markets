def show_output(markets: list):
    if markets:
        for market in markets:
            x = """
            Market №{fmid}
                "{marketname}"
            Rating: {rate}
            Address:
                {street}, {city}, {county}, {state}, {zip}
            Categories:
                {categories}
            Payments:
                {payments}
            Seasons:
                season1 - {season1} {season1_time}
                season2 - {season2} {season2_time}
                season3 - {season3} {season3_time}
                season4 - {season4} {season4_time}
            Media:
                youtube - {youtube}
                facebook - {facebook}
                website - {website}
                othermedia - {othermedia}
            \n
            """.format(**market)
            print(x)
    else:
        print("No markets were found")
