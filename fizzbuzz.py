def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


for num in range(1, 101):
    print(fizzbuzz(num))

import calc

calc.add(1, 2)

from calc import add

print(add(1, 2))


import calc as c

print(c.add(1, 2))

from calc import add, sub

print(add(1, 2))

print(sub(2, 1))

import datetime
d = datetime.date(2016,12,23)
print(d.year,d.month,d.day)

today = datetime.date.today()
print(today)

birthday = datetime.date(2013,10,4)
today = datetime.date.today()
delta = today - birthday
print(delta.days)

import re
m = re.search('(P(ythll)IZ)o[pn]e?','Python')
m



m = re.search('py(thon)','python')
m.group()

m.group(1)

re.search('py','ruby')



# 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


