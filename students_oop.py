import sys

class Students:
    def __init__(self, name, house, patronos):
        if not name:
            raise ValueError("Invalid Name")
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid house")
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
        

def main():
    student = getStudent()
    print(student)
    print("Expecto Patronom!")
    print(student.charm())

def getStudent():
    name = input("Enter name: ")
    house = input("Enter house: ")
    patronos = input("Enter a patronos: ")
    try:
        return Students(name, house, patronos)
    except ValueError as e:
        print(e)
        sys.exit()
    

if __name__ == "__main__":
    main()
