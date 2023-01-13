def show_output(markets):
    if markets:
        for market in markets:
            x = "№{fmid}: \"{marketname}\"".format(**market)
            print(x)
    else:
        print("No markets were found")


if __name__ == "__main__":
    pass
