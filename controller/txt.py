GREETINGS = """

                ***Welcome to the FarmMarkets application!***
        Here you can find all informations about farmers markets you interested
        -----------------------------------------------------------------------

        Enter [guide] command to get instruction

        """


GUIDE = """
        Application supports next features:

        --  command [list 'sort_mode' 'reverse'] allows you to get sorted (FMID, MarketName, average rating) of all markets in US.
            Modes:
                '1' <- Sorted by FMID
                '2' <- Sorted by MarketName (default)
                '3' <- Sorted by rating
            Reverse:
                '+' <- Reverse False (default)
                '-' <- Reverse True
            Examples:
                ==> Enter a command: list
                ==> Enter a command: list 1 +
                ==> Enter a command: list 3 -
            ;
        --  command [find *('filter_mode' 'value')] allows you to put a few filters and get (FMID, MarketName) markets matched your request.
            Filters:
                1 <- Filtered by city
                2 <- Filtered by state
                3 <- Filtered by zip
            Examples:
                ==> Enter a command: find 1 Miami
                ==> Enter a command: 1 Danville 2 Vermont
                ==> Enter a command: find 3 70062 3 57064
            ;
        --  command [show 'FMID'] allows you to get full info about specific market.
            ;
        --  command [add_review 'FMID'] allows you to leave a rating and write review about specific market.
            ;
        --  command [exit] makes exit from application.

        """


BYE = """
        Thank you for using FarmMarkets application!
        Good Bye!

        """
