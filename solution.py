class Book:
    def __init__(self, id, score, cont):
        self.id = id
        self.score = score

class Lib:
    def __init__(self, id, size, books, signup, ship, available):
        self.id = id
        self.size = size
        self.books = books # vector<book>
        self.signup = signup
        self.ship = ship
        self.available = available

def scorelib(lib):
    total = 0
    for x in lib.books:
        total += x.score
    return ((total/lib.ship) + lib.signup)

f = open('a.txt', 'r')
l1 = f.readline()
l1 = l1.replace('\n', '')
l1 = l1.split(' ')
b = int(l1[0]) #nombre de llibres diferents
print(str(b)+": llibres diferents")
l = int(l1[1]) #nombre de llibreries
print(str(l)+": num llibreries")
d = int(l1[2]) # nombre de dies
print(str(d)+": num dies")
l2 = f.readline()
l2 = l2.replace('\n', '')
l2 = l2.split(' ')
vectorllibres = [] # vector amb tots els llibres
for x in range(len(l2)):
    library = [] #vector de llibreries que el contenen (per defecte vuit)
    book = Book(x, int(l2[x]), library)
    vectorllibres.append(book)
print("Tots el llibres :")
for x in vectorllibres:
    print("id del llibre: " + str(x.id))
    print("score del llibre: " + str(x.score))
vectorllibreries = []
for x in range(l):

    #per a cada llibreria
    l3 = f.readline()
    l3 = l3.replace('\n', '')
    l3 = l3.split(' ')
    n = int(l3[0]) #numero de llibres a la llibreria
    t = int(l3[1]) # nombre de dies (ship)
    m = int(l3[2]) # nombre de llibres cada dia
    l4 = f.readline()
    l4 = l4.replace('\n', '')
    nbooks = l4.split(' ') # vector amb el id dels llibres --> ves en compte has d'utilitzar int()
    llibreria = Lib(x, )
