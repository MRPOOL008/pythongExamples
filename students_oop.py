class Students:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        

def main():
    student = getStudent()
    print(f"Hi {student.name} from {student.house}")

def getStudent():
    name = input("Enter name: ")
    house = input("Enter house: ")
    student = Students(name, house)
    return student

if __name__ == "__main__":
    main()