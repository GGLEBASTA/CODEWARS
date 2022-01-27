def open_or_senior(data):
    s = 0
    n = 0
    cc = []
    age = []
    handi = []
    for i in data:
        for z in i:
            if(s == 0):
                age.append(z)
                s = s + 1
                n = n + 1
                continue
            elif(s != 0):
                handi.append(z)
                s = 0
                continue
            
    

    k = 0
    while n > 0:
        if((age[k]>=55) and (handi[k]>7)):
            cc.append('Senior')
            n = n - 1
            k = k + 1
        else:
            cc.append('Open')
            n = n - 1
            k = k + 1

    return cc


m = open_or_senior([(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)])
print(m)