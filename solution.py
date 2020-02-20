class Book:
    def __init__(self, id, score, cont):
        self.id = id
        self.score = score
        self.cont = cont # vector<Lib>: són les llibreries que el contenen

class Lib:
    def __init__(self, id, signup, ship, available):
        self.id = id
        self.signup = signup
        self.ship = ship
        self.available = available

