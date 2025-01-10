class Wizard: 
    def __init__(self, name):
        if not name:
            raise ValueError("No name provided!")
        self.name = name

class Students(Wizard): 
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject