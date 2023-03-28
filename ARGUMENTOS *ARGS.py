
def world_cup_titles(country, *args):
    print("Country:",country)

    for title in args:
        print("year:",title)

world_cup_titles("Brasil","1958","1962","1970","1994","2002")

