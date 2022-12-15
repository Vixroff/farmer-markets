def greetings():
    print(
        """

                ***Welcome to the FarmMarkets application!***
        Here you can find all informations about farmers markets you interested
        -----------------------------------------------------------------------
        """
        )
    

def guide():
    print(
        """
        Application supports next features:

        --  command [list] allows you to get (FMID, MarketName, average rate) of all markets in US;

        --  command [find 'filter' 'value'] allows you to put filters and get (FMID, MarketName) markets matched for search
            Filters:
                1 - city
                2 - state
                3 - zip
            Examples:
                ==> Enter a command: find 1 Miami
                ==> Enter a command: find 2 New York
                ==> Enter a command: find 3 70062
            ;
        --  command [show 'FMID'] allows you to get full info about specific market;

        --  command [add_review 'FMID'] allows you to leave a rating and write review about specific market; 

        
                

        """
        )   


def main():
    greetings()



if __name__ == "__main__":
    main()