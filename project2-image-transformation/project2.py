def generate_random(row, column):
    from random import randint
    l = []
    if 1<=row<=100 and 1<=column<=100:
        for i in range(column):
                l.append([{'red': randint(0,255),'green': randint(0,255), 'blue': randint(0,255)} for j in range(row)])
        return l
    else:
        return "your column or row is not between 1 and 100"

def is_valid(img):
    l = [[*j.values()] for i in img for j in i]
    for i in l:
        for j in i:
            if not 0<=j<=255 or type(j) == float:
                return False
    return True

def read_from_file(filename):
    try:
        with open(filename,"r") as file:
            x = file.readlines()
            l = [[{"red" : int(j[k][0:2], 16), "green" : int(j[k][2:4], 16), "blue" : int(j[k][4:], 16)} for k in range(len(j))] for j in [i.strip().split(", ") for i in x]]
            return l
    except FileNotFoundError:
        return "file not found"

def write_to_file(img, filename):
    file = open(filename,"w")
    l = [", ".join(k) + "\n" for k in [["".join(j) for j in i] for i in [[["0" + hex(k)[2:].upper() if len(hex(k)[2:]) < 2 else hex(k)[2:].upper() for k in [*j.values()]] for j in i] for i in img]]]
    l[-1] = l[-1][:-1]
    for i in l:
        file.write(i)
    file.close()

def clear(img):
    l = img.copy()
    for i in l:
        for j in i:
            for k in j:
                j[k] = 0
    img.clear()
    img.extend(l)

def set_value(img, value, channel='rgb'):
    if 0<=value<=255:
        c = sorted([i for i in channel if i == 'r' or i == 'g' or i == 'b'], reverse=True)
        l = img.copy()
        for i in l:
            for j in i:
                for k in c:
                    if k == "r":
                        j["red"] = value
                    elif k == "g":
                        j["green"] = value
                    else:
                        j["blue"] = value
        img.clear()
        img.extend(l)

def fix(img):
    if is_valid(img) == False:
        l = img.copy()
        for i in l:
            for j in i:
                for k in j:
                    if 0 > j[k]:
                        j[k] = 0
                    elif j[k] > 255:
                        j[k] = 255
                    else:
                        j[k] = round(j[k])
        img.clear()
        img.extend(l)

def rotate90(img):
    liste = []
    for j in range(len(img[0])):
        a = [img[i][j] for i in range(len(img) - 1, -1, -1)]
        liste.append(a)
    return liste

def rotate180(img):
    l = rotate90(rotate90(img))
    return l

def rotate270(img):
    l = rotate180(rotate90(img))
    return l

def mirror_x(img):
    l = []
    for i in img:
        l.append(i[::-1])
    img.clear()
    img.extend(l)

def mirror_y(img):
    l = img.copy()[::-1]
    img.clear()
    img.extend(l)

def enhance(img, value, channel='rgb'):
    if 0<value and type(value) == float:
        c = sorted([i for i in channel if i == 'r' or i == 'g' or i == 'b'], reverse=True)
        l = img.copy()
        for i in l:
            for j in i:
                for k in c:
                    if k == "r":
                        j["red"] = round(j["red"]*value)
                    elif k == "g":
                        j["green"] = round(j["green"]*value)
                    else:
                        j["blue"] = round(j["blue"]*value)
        img.clear()
        img.extend(l)

def grayscale(img, mode=1):
    l = img.copy()
    for i in l:
        for j in i:
            a, b, c = j["red"],  j["green"], j["blue"]
            if mode == 1:
                j["red"], j["green"], j["blue"] = round((a + b + c)/3), round((a + b + c)/3), round((a + b + c)/3)
            elif mode == 2:
                j["red"], j["green"], j["blue"] = round(a*0.299 + b*0.587 + c*0.114), round(a*0.299 + b*0.587 + c*0.114), round(a*0.299 + b*0.587 + c*0.114)
            elif mode == 3:
                j["red"], j["green"], j["blue"] = round(a*0.2126 + b*0.7152 + c*0.0722), round(a*0.2126 + b*0.7152 + c*0.0722), round(a*0.2126 + b*0.7152 + c*0.0722)
            elif mode == 4:
                j["red"], j["green"], j["blue"] = round(a*0.2627 + b*0.6780 + c*0.0593), round(a*0.2627 + b*0.6780 + c*0.0593), round(a*0.2627 + b*0.6780 + c*0.0593)
    img.clear()
    img.extend(l)

def get_freq(img, channel='rgb', bin_size=16):
    l = [[[*range(0,256,bin_size)][j],[*range(0,256,bin_size)][j+1]-1] for j in range(len([*range(0,256,bin_size)])-1)] if bin_size != 0 else ""
    "" if bin_size == 0 else l.append([0,255]) if bin_size == 256 else l.append([l[-1][-1]+1, 255])
    c = sorted([i for i in channel if i == 'r' or i == 'g' or i == 'b'], reverse=True)
    cntrl, l1 = {"r": [], "g": [], "b": []}, {"r": [], "g": [], "b": []}
    for i in img:
        for k in i:
            for m in c:
                cntrl[m].append(k["red"] if m == "r" else k["green"] if m == "g" else k["blue"])
                cntrl[m].sort()
    for i in c:
        for j in l:
            counter = 0
            for k in cntrl[i]:
                if j[0] <= k <= j[1]:
                    counter += 1
            if counter:
                l1[i].append(counter)
            if not counter:
                l1[i].append(0)
    cntrl = {"bins" : l}
    for i in c:
        if i == "r":
            cntrl["red"] = l1[i]
        if i == "g":
            cntrl["green"] = l1[i]
        if i == "b":
            cntrl["blue"] = l1[i]
    return cntrl

def scale_down(img, N):
    l = []
    for i in img:
        while len(i)%N != 0:
            i.append(i[-1])
        l.append([i[N*j:N*(j+1)] for j in range(0, int(len(i)/N))])
    if len(l)%N != 0:
        l.append(l[-1])
    l1 = []
    for i in range(int(len(l)/N)):
        l1.append([])
        for j in range(len(l[0])):
            l1[i].append([])
            for k in l[i*N:(i+1)*N]:
                l1[i][j].extend(k[j])
    l.clear()
    l = [[{"red": round(sum([k["red"] for k in j]) / (N**2)), "green": round(sum([k["green"] for k in j]) / (N**2)), "blue": round(sum([k["blue"] for k in j]) / (N**2))} for j in i] for i in l1]
    return l

def scale_up(img, N):
    l = [k for k in [[j for j in i for c in range(N)] for i in img] for m in range(N)]
    return l

def apply_window(img, window):
    c = len(img[0])
    l = []
    for i in range(len(img)):
        for j in range(2):
            if j == 0:
                (img[i]).insert(0, img[i][0])
            if j == 1:
                (img[i]).insert(c, img[i][c])
    img.insert(0, img[0])
    img.insert(-1, img[len(img) - 1])
    for i in range(1,len(img)-1):
        l.append([])
        for j in range(1,len(img[0])-1):
            l[i-1].append([])
            for k in img[i-1:i+2]:
                l[i-1][int(j-1)].extend(k[j-1:j+2])
    window = [j for i in window for j in i]
    for i in l:
        for j in i:
            l[l.index(i)][i.index(j)] = {"red": round(sum([j[c]["red"]*window[c] for c in range(len(j))])), "green": round(sum([j[c]["green"]*window[c] for c in range(len(j))])),"blue": round(sum([j[c]["blue"]*window[c] for c in range(len(j))]))}
    fix(l)
    return l