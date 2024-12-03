import sys

class Students:
    def __init__(self, name, house, patronos):
        self.name = name
        self.house = house
        self.patronos = patronos

    def __str__(self):
        return f"Hi {self.name} from the house {self.house}"
    
    def charm(self):
        match self.patronos:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case _:
                return "🪄"

    @property
    def name(self):
        return self._name

    #setter name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid Name")
        self._name = name

    @property
    def house(self):
        return self._house

    #setter house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Enter name: ")
        house = input("Enter house: ")
        patronos = input("Enter a patronos: ")
        return cls(name, house, patronos)
        

def main():
    try:
        student = Students.get()
        print(student)
        print("Expecto Patronom!")
        print(student.charm())
    except ValueError as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    main()
