class Book:
    def __init__(self, id, score, selected):
        self.id = id
        self.score = score
        self.selected = selected

class Lib:
    def __init__(self, id, size, books, signup, ship):
        self.id = id
        self.size = size
        self.books = books # vector<book>
        self.signup = signup
        self.ship = ship
#Obtenir el millor llibre de la llibreria
def getBestBookId(lib):
    maxscore = -1
    maxid = -1
    for book in lib.books:
        if book.score>maxscore:
            maxscore = book.score
            maxid = book.id
    return maxid

#elimina del vector un id
def removeBook(vectorbooks, id):
    for i in range(len(vectorbooks)):
        if id == vectorbooks[i].id:
            vectorbooks.pop(i)
            return vectorbooks
#Elimina del vector un id
def removeLibrary(vectorlibrary, id):
    for i in range(len(vectorlibrary)):
        if id == vectorlibrary[i].id:
            vectorlibrary.pop(i)
            return vectorlibrary


#Score de la llibreria
def scorelib(lib):
    total = 0
    for book in lib.books:
        if (book.selected == False):
            total += book.score
    return total

def get_best_bookselect(bookstotal, bookslibrary):
    bestbook = Book(-1, -1, False)
    for book in bookstotal:
        if book in bookslibrary and book.score>bestbook.score and book.selected == False:
            bestbook = book
    if bestbook.score == -1:
        return bookslibrary[0]
    else:
        bestbook.selected = True
        return bestbook





def sort_by_scorelib(libraries):
    libraries.sort(key=scorelib, reverse=True)
    return libraries

def score_comp(book):
    return book.score

def sort_books(books):
    books.sort(key=score_comp, reverse=True)
    return books

def wanted(books, book):
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

f = open('c.txt', 'r')
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
    book = Book(x, int(l2[x]), False)
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
    for i in range(len(l3)):
        booksv.append(vectorllibres[int(l3[i])])
    n = int(l3[0]) #numero de llibres a la llibreria
    t = int(l3[1]) # nombre de dies (ship)
    m = int(l3[2]) # nombre de llibres cada dia
    l4 = f.readline()
    l4 = l4.replace('\n', '')
    nbooks = l4.split(' ') # vector amb el id dels llibres --> ves en compte has d'utilitzar int()

    llibreria = Lib(x, n, booksv,t, m)
    print("Llibreria: n= "+str(n)+" t = "+str(t)+" m= "+str(m))
    vectorllibreries.append(llibreria)

day = 0
idllibreriaactual = -1

#Ordena les llibreries
vectorllibreries.sort(key=lambda x: scorelib(x), reverse=True)
for library in vectorllibreries:
    #comença amb la primera llibreria
    idllibreriaactual = vectorllibreries[0].id
    day+=library.signup
    booksxday = library.ship
    for i in booksxday:




#print(score)