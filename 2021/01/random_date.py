from random import randint, randrange, choice
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (start + timedelta(seconds=random_second)).date()

d1 = datetime.strptime('1.1.2000', '%d.%m.%Y')
d2 = datetime.strptime('1.1.2021', '%d.%m.%Y')

dates = []

for i in range(500):
    dates.append(random_date(d1, d2).strftime("%d.%m.%Y"))

for i in range(20):
    index = randint(0, 499)
    dates[index] = dates[index].replace(".", ",", randint(1, 2))

for i in range(20):
    index = randint(0, 499)
    if(randint(0, 1) == 0):
        dates[index] = dates[index] + ' '
    else:
        dates[index] = ' ' + dates[index]

outputfile = open("dates.txt", "w")
for date in dates:
    outputfile.write(date + "\n")
outputfile.close()