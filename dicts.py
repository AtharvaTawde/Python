scores = {
    "Aaryan": {"0": "2", "1": "3"}, 
    "bruh": {"0": "1241332"}, 
    "this is so dumb": {"0": "10810"}}

scorelist = []
keylist = []
klist = []
kvlist = []

for key, dict in scores.items():
    keylist.append(key)
    for k, v in dict.items():
        klist.append(int(k))
        scorelist.append(int(v))
        index = k + v
        kvlist.append(index)

print(keylist)
print(scorelist)
highscore = max(scorelist)
print(highscore)

findk = klist[scorelist.index(highscore)]
print(findk)

print(kvlist)
findK = keylist[kvlist.index(str(findk) + str(highscore)) - 1]
print(findK, highscore)