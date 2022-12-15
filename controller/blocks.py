GREETINGS = """

                ***Welcome to the FarmMarkets application!***
        Here you can find all informations about farmers markets you interested
        -----------------------------------------------------------------------

        Enter [guide] command to get instruction
        """

 
GUIDE = """
        Application supports next features:

        --  command [list 'sort'] allows you to get sorted (FMID, MarketName, average rating) of all markets in US
            Sortes:
                1 <- FMID
                2 <- MarketName
                3 <- rating
            Examples:
                ==> Enter a command: list 1
            ;
        --  command [find *('filter' 'value')] allows you to put filters and get (FMID, MarketName) markets matched for search
            Filters:
                1 <- city
                2 <- state
                3 <- zip
            Examples:
                ==> Enter a command: find 1 Miami
                ==> Enter a command: 1 Danville 2 Vermont
                ==> Enter a command: find 3 70062 3 57064
            ;
        --  command [show 'FMID'] allows you to get full info about specific market;
            ;
        --  command [add_review 'FMID'] allows you to leave a rating and write review about specific market;
            ;
        --  command [exit] makes exit from application;
        """
