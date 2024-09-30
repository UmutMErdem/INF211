def problem1(l, n):
    if l:
        s = set(l)
        d = {}
        for i in s:
            d[i] = l.count(i)
        c = max(d.values())
        if n >= 1 and n <= c:
            return [i for i in d if d[i] == n]
    return []

def problem2(l):
    if l:
        cntrl = []
        for i in l:
            cntrl.append(l[i])
        cntrl.sort()
        if len(cntrl) % 2 == 0:
            median = (cntrl[int(len(cntrl)/2-1)] + cntrl[int(len(cntrl)/2)])/2
            return median
        return cntrl[int((len(cntrl)-1)/2)]
    return 0

def problem3(f):
    try:
        with open(f, "r") as file:
            if file:
                l = []
                for i in file.readlines():
                    for j in i:
                        if " " == j:
                            i = i[:i.index(j)] + i[i.index(j)+1:]
                    a = i.split(",")
                    if a[-1] == "\n":
                        a[-1] = "NA"
                    else:
                        a[-1] = a[-1][:-1]
                    l.append({"name" : a[0], "credit" : int(a[1]), "term" : int(a[2]), "grade" : a[3]})
                return l
            else:
                return []
    except:
        return []

def problem4(d,t):
    notes = {'AA': 4.0, 'BA': 3.5, 'BB': 3.0, 'CB': 2.5, 'CC': 2.0, 'DC': 1.5, 'DD': 1.0, 'FF': 0.0, 'NA': 'NA'}
    gpa = 0
    credit = 0
    if d:
        for i in d:
            if i["term"] == t:
                if i["grade"] == "NA":
                    continue
                gpa += notes[i["grade"]] * i["credit"]
                credit += i["credit"]
        if not credit:
            return 0
        return gpa / credit
    else:
        return 0

def problem5(ffunc, n):
    l=[]
    for i in range(n+1):
        if "1" in str(i)[:]:
            l.append(str(i))
    toplam = 0
    for i in l:
        toplam += i.count("1")
    if ffunc == toplam:
        return True
    else:
        return False

def problem6(s):
    karakterler = tuple(s.lower())
    n = len(karakterler)
    l = []
    karakterler1 = [tuple(range(n))] * n
    sonuc = [[]]
    for i in karakterler1:
        sonuc = [x + [y] for x in sonuc for y in range(n)]
        l.append(sonuc)
    a = 1
    x = set()
    for i in l:
        for j in i:
            s = ""
            if len(set(j)) == a:
                for k in j:
                    s += karakterler[k]
                x.add(s)
        a += 1
    l = sorted(i for i in x)
    return l

def problem7(s, f):
    try:
        with open(f, "r") as file:
            a = file.read()
            if a:
                if s.lower() in a:
                    return problem6(s)
            else:
                return []
    except:
        return []

def problem8(m, n):
    l = []
    f = 3
    f1 = 4
    counter = 0
    a = 0
    while a < f:
        b = a + 1
        while b <= f:
            c = 0
            while c < f1:
                b = c + 1
                while b <= f1:
                    l1 = []
                    for i in m[a:b]:
                        l1.append(i[c:b])
                    l.append(l1)
                    counter += 1
                    b += 1
                c += 1
            b += 1
        a += 1
    for i in l:
        if i == n:
            return True
    return False

def problem9(s):
    a = s[0]
    l = []
    counter = ""
    x = ""
    for i in range(len(s)):
        if s[i] == a:
            counter += s[i]
        else:
            l.append(counter)
            counter = s[i]
            a = s[i]
    l.append(counter)
    for i in l:
        x += i[0]
        if len(i) > 1:
            x += str(len(i))
    return (x, int((len(s)-len(x))*100/len(s)))

def problem10(a):
    a.sort()
    index = 0
    for i in range(min(a),max(a)+1):
        if i != a[index]:
            return i
        index += 1
    return max(a) + 1