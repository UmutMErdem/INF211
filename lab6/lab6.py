def problem0():
    class p0:
        def __init__(self, x):
            self.x = x
        def get_value(self):
            return self.x
        def set_value(self, y):
            self.x = y
    return p0

def problem1():
    class p1:
        def __init__(self, x):
            if type(x) == int:
                self.x = x
            else:
                self.x = 0
        def get_value(self):
            return self.x
        def set_value(self, x):
            if type(x) == int:
                self.x = x
    return p1

def problem2():
    class p1:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def get_area(self):
            area = self.x*self.y
            return area
        def get_perimeter(self):
            perimeter = 2*(self.x+self.y)
            return perimeter
    return p1

def problem3():
    class Grades:
        def __init__(self):
            self.l = [0.0]
        def add_grade(self, x):
            self.l.append(x)
            if 0.0 in self.l:
                self.l.remove(0.0)
            self.l.sort()
        def remove_grade(self, x):
            if x in self.l:
                self.l.remove(x)
        def get_min(self):
            return float(min(self.l))
        def get_max(self):
            return float(max(self.l))
        def get_mean(self):
            return float(sum(self.l)/len(self.l))
        def get_median(self):
            if len(self.l)%2 == 0:
                return float((self.l[int(len(self.l)/2)-1] + self.l[int(len(self.l)/2)])/2)
            else:
                return float(self.l[int((len(self.l)-1)/2)])
    return Grades

def problem4():
    class Movie:
        def __init__(self, mandatory, optional):
            if type(mandatory[0]) == str:
                self.movie_name = mandatory[0]
            if type(mandatory[1]) == str:
                self.director = mandatory[1]
            if 1920 <= mandatory[2] <= 2021:
                self.year = mandatory[2]
            if type(optional[0]) == float and 0.0 <= optional[0] <= 10.0:
                self.rating = optional[0]
            else:
                self.rating = 0.0
            if type(optional[1]) == int and 0 <= optional[1] <= 500:
                self.length = optional[1]
            else:
                self.length = 0
        def get_movie_name(self):
            return self.movie_name
        def get_director(self):
            return self.director
        def get_year(self):
            return self.year
        def get_rating(self):
            return self.rating
        def get_length(self):
            return self.length
        def set_rating(self, x):
            if type(x) == float and 0.0 <= x <= 10.0:
                self.rating = x
        def set_length(self, x):
            if type(x) == int and 0 <= x <= 500:
                self.length = x
    return Movie

def problem5():
    class MovieCatalog:
        def __init__(self, filename):
            self.a = problem4()
            self.filename = open(filename,"r+")
            r =  [i.strip("\n").split(",") for i in self.filename.readlines()]
            self.ml = []
            for i in r:
                b = self.a([i[0], i[1], int(i[2])], [float(i[3]), int(i[4])])
                self.ml.append({"movie_name":b.get_movie_name(), "director":b.get_director(), "year":b.get_year(), "rating":b.get_rating(), "length":b.get_length()})
            self.filename.close()
        def add_movie(self, movie_name, director, year, rating=0.0, length=0):
            b = self.a([movie_name, director, year], [rating, length])
            if {"movie_name":b.get_movie_name(), "director":b.get_director(), "year":b.get_year(), "rating":b.get_rating(), "length":b.get_length()} not in self.ml:
                self.ml.append({"movie_name":b.get_movie_name(), "director":b.get_director(), "year":b.get_year(), "rating":b.get_rating(), "length":b.get_length()})
        def remove_movie(self, movie_name):
            for i in self.ml:
                if i["movie_name"] == movie_name:
                    self.ml.remove(i)
        def get_oldest(self):
            old = [i["movie_name"] for i in self.ml if i["year"] == min([i["year"] for i in self.ml])]
            return ", ".join(old)
        def get_lowest_ranking(self):
            low = [i["movie_name"] for i in self.ml if i["rating"] == min([i["rating"] for i in self.ml])]
            return ", ".join(low)
        def get_highest_ranking(self):
            high = [i["movie_name"] for i in self.ml if i["rating"] == max([i["rating"] for i in self.ml])]
            return ", ".join(high)
        def get_by_director(self, director):
            r = []
            for i in self.ml:
                if director == i["director"]:
                    r.append(i["movie_name"])
            return r
    return MovieCatalog

def problem6():
    class Node:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        def get_node(self):
            return (self.x, self.y, self.z)
        def get_distance(self):
            return ((self.x)**2+(self.y)**2+(self.z)**2)**0.5
        def __add__(self, other):
            a = self.x + other.x
            b = self.y + other.y
            c = self.z + other.z
            return Node(a, b, c)
        def __str__(self):
            return f'<{self.x}, {self.y}, {self.z}>'
        def __gt__(self, other):
            if Node.get_distance(self) > ((other.x)**2+(other.y)**2+(other.z)**2)**0.5:
                return True
            else:
                return False
        def __ge__(self, other):
            if Node.get_distance(self) >= ((other.x)**2+(other.y)**2+(other.z)**2)**0.5:
                return True
            else:
                return False
        def __lt__(self, other):
            if Node.get_distance(self) < ((other.x)**2+(other.y)**2+(other.z)**2)**0.5:
                return True
            else:
                return False
        def __le__(self, other):
            if Node.get_distance(self) <= ((other.x)**2+(other.y)**2+(other.z)**2)**0.5:
                return True
            else:
                return False
        def __eq__(self, other):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
            else:
                return False
    return Node

def problem7():
    from random import randint
    class NodeCloud:
        def __init__(self, n):
            self.n = n
            self.l = [(randint(-20,20), randint(-20,20), randint(-20,20))for i in range(n)]
        def get_nodes(self):
            return self.l
        def get_outermost(self):
            order = {}
            a = problem6()
            for i in self.l:
                order[a(x=i[0],y=i[1],z=i[2]).get_distance()] = i
            return [i[1] for i in sorted(order.items(),key=lambda x:x[0])][-1]
        def add_node(self, x, y, z):
            self.l.append((x, y, z)) if (x, y, z) not in self.l else ""
        def get_sum(self):
            a, b= problem6(), problem6()
            a1 = a(0,0,0)
            for i in self.l:
                a1 = a1 + b(i[0],i[1],i[2])
            return a1.get_node()
    return NodeCloud

def problem8():
    class Encoder:
        def __init__(self, x):
            chars = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + [chr(j) for j in range(48,58)]
            self.x = "".join([i for i in x if i in chars])
        def __str__(self):
            return self.x
        def morse(self):
            mcd = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
            em = [mcd[letter.upper()] for letter in self.x]
            return em
        def binary(self):
            bv = "".join([bin(ord(i))[2:] for i in self.x])
            return bv
        def hex(self):
            hv = "".join([hex(ord(i))[2:] for i in self.x])
            return hv
    return Encoder