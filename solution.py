class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Lib:
    def __init__(self, id, size, books, signup, ship):
        self.id = id
        self.size = size
        self.books = books # vector<book>
        self.signup = signup
        self.ship = ship

def scorelib(lib):
    total = 0
    for x in lib.books:
        total += x.score
    return ((total/lib.ship) + lib.signup)

def sort_by_scorelib(libraries):
    libraries.sort(key=scorelib, reverse=True)
    return libraries

def cut_libraries(libraries, d):
    total = 0
    definitive = []
    while ((total < d) and len(libraries) != 0):
        lib = libraries.pop(0)
        total += lib.signup
        if (total < d):
            definitive.append(lib)
    return definitive

def score_comp(book):
    return book.score

def sort_lib_books(library):
    library.books.sort(key=score_comp, reverse=True)
    return library

def wanted_bo(books, book):
    iz = 0
    de = len(books) - 1
    while (iz <= de):
        mid = int((iz + de) / 2)
        if (books[mid].id == book.id):
            return True
        elif (books[mid].id < book.id):
            de = mid - 1
        else:
            iz = mid + 1
    return False

def wanted(books, book):
    for x in books:
        if (book.id == x.id):
            return True
    return False

def print_lib(lib):
    print(lib.id, end=' ')
    print(len(lib.books))
    for book in lib.books:
        print(book.id, end=' ')
    print()

seleccio = input("Quin test case proves: ")
if (seleccio == 'a'):
    f = open('a.txt', 'r')
elif (seleccio == 'b'):
    f = open('b.txt', 'r')
elif (seleccio == 'c'):
    f = open('c.txt', 'r')
elif (seleccio == 'd'):
    f = open('d.txt', 'r')
elif (seleccio == 'e'):
    f = open('e.txt', 'r')
elif (seleccio == 'f'):
    f = open('f.txt', 'r')
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
    book = Book(x, int(l2[x]))
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
    booksv = []  # vector de llibres per la llibreria
    n = int(l3[0]) #numero de llibres a la llibreria
    t = int(l3[1]) # nombre de dies (ship)
    m = int(l3[2]) # nombre de llibres cada dia
    l4 = f.readline()
    l4 = l4.replace('\n', '')
    nbooks = l4.split(' ') # vector amb el id dels llibres --> ves en compte has d'utilitzar int()
    for i in range(len(nbooks)):
        booksv.append(vectorllibres[int(nbooks[i])])
    llibreria = Lib(x, n, booksv,t, m)
    print("Llibreria: n= "+str(n)+" t = "+str(t)+" m= "+str(m))
    vectorllibreries.append(llibreria)

vectorllibreries = sort_by_scorelib(vectorllibreries)
vectorllibreries = cut_libraries(vectorllibreries, d)

print(len(vectorllibreries))

for lib in vectorllibreries:
    lib = sort_lib_books(lib)
    output = []
    for i in range(len(lib.books)):
        if wanted(vectorllibres, lib.books[i]):
            output.append(lib.books[i])
            vectorllibres.remove(lib.books[i])
    lib.books = output
    print_lib(lib)