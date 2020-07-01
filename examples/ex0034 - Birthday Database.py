import json

with open("birthDict.json", "r") as f:
    birthdays = json.load(f)

while True:
    choice = input("Would you like to retrieve birthdays, delete values or append values from the existing dictionary? Type R to retrieve, D to delete or A to append: ")
    
    if choice in 'Rr':
        
        print('\n')
        for key in birthdays.keys():
            print(key)
        print('\n')
        
        name = input('Type in the name of the individual listed below to retrieve their birthdate.\n')

        try:
            date = birthdays[name]
            print(name + "'s birthday is", date + '.')

        except:
            print("You have entered an individual's name that is not in this list.\n")
    
    if choice in 'Dd':
        
        print('\n')
        for key in birthdays.keys():
            print(key)
        print('\n')

        while True:
            deletePerson = input("Enter name of individual who you would like to delete from the dictionary: \n")
            
            try:
                birthdays.pop(deletePerson)

                with open("birthDict.json", "w") as f:
                    json.dump(birthdays, f)
            
                print('Deletions to dictionary made.\n')
            
            except:
                print('Person not found in dictionary.')
                continue
            
            ex = input("Do you want to exit deleting mode? Type Y or N exactly as shown: ")
            if ex in 'Yy':
                break
            else:
                continue
    
    if choice in 'Aa':
        
        print('\n')
        for key in birthdays.keys():
            print(key)
        print('\n')
        
        while True:
            newPerson = input("Enter name of individual who you would like to add to the dictionary: \n")
            newDate = input("Enter birthdate of individual who you would like to add to the dictionary: \n")
            
            newEntry = {newPerson: newDate}

            birthdays.update(newEntry)

            with open("birthDict.json", "w") as f:
                json.dump(birthdays, f)
            
            print('Additions to dictionary made.\n')
            
            ex = input("Do you want to exit appending mode? Type Y or N exactly as shown: ")
            if ex in 'Yy':
                break
            else:
                continue