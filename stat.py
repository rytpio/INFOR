import datetime


def quarter(date: str, separator: str, month_position: int):
    d1 = [int(x) for x in date.split(separator)]
    #d = datetime.date(d1[2], d1[0], d1[1])

    month = d1[month_position]
    match month:
        case month if month <= 3:
            q = 1
        case month if month <= 6:
            q = 2
        case month if month <= 9:
            q = 3
        case month if month <= 12:
            q = 4
        case _:
            q = 1

    return q


#print(quarter('1/01/2022', '/', 0))
assert quarter('1/01/2022', '/', 0) == 1
assert quarter('6/01/2022', '/', 0) == 2
assert quarter('8/01/2022', '/', 0) == 3
assert quarter('10/01/2022', '/', 0) == 4


#get material data
#get quarter data
#get stat data - need sql stat db;
#combine on basis of group_mask - need sql key db
#input wanted result - show data updated to latest quarter avaiable
#show data updated to next years-based on what? prognosis? inflation? - need additional data
#option to spit out future stats data input for "prognosed" input and recalculate :?