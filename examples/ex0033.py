birthdays = {
    'Albert Einstein': '03/14/1879',
    'Ada Lovelace': '12/10/1815',
    'Benjamin Franklin': '01/17/1706'
}

while True:
    print('Type in the name of the individual listed below to retrieve their birthdate.\n')
    for key in birthdays.keys():
        print(key)

    name = input('\n')

    try:
        date = birthdays[name]
        print(name + "'s birthday is", date + '.')

    except:
        print("You have entered an individual's name that is not in this list.\n")