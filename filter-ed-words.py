with open('allwords.txt') as allwords:
    allwords = allwords.readlines()
pastwords = []
for word in allwords:
    allwordss = []
    allwordss.append(word)
    print(allwordss)
    nos = allwordss[0].strip("\ ")
    res = nos.endswith("edn")
    print(nos)

    #if "n" in cut:
    #pastwords.append(nonl)
print(pastwords)