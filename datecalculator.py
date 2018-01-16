import datetime
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

d = datetime.datetime.now()
next_friday = next_weekday(d, 4).date() # 0 = Monday, 1=Tuesday, 2=Wednesday...
print(next_friday)
