class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Lib:
    def __init__(self, books, signup, ship):
        self.books = books
        self.signup = signup
        self.ship = ship