class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Lib:
    def __init__(self, books, size, signup, ship):
        self.books = books # vector<Book>
        self.size = size
        self.signup = signup
        self.ship = ship

