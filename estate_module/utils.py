import datetime

def diff_between_two_dates(d1, d2):
    date_format = "%m/%d/%Y, %H:%M:%S"
    a = d1.strftime(date_format)
    b = d2.strftime(date_format)
    d1 = datetime.datetime.strptime(str(b), date_format)
    d2 = datetime.datetime.strptime(str(a), date_format)
    delta = d2 - d1
    return delta