import json
from collections import Counter

#pure idiocy, can be optimized later
MONTHS = ['January', 'February', 'March', 'April', 
        'May', 'June', 'July', 'August', 
        'September', 'October', 'November', 'December']

dictIndex = ['01', '02', '03', '04', 
            '05', '06', '07', '08', 
            '09', '10', '11', '12']

months = []

x = "birthDict.json"

with open(x, "r") as f:
    birthdays = json.load(f)

for date in birthdays.values():
    date = date.split('/')
    months.append(date[0])

months = Counter(months)

print("According to", x + ", there are:\n")

for i in range(12):
    month = MONTHS[i]
    index = dictIndex[i]
    print('{} birthdays in'.format(months[index]), month + '.')