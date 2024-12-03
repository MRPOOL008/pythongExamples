import random

class Hat:
    
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"] 

    @classmethod
    def sort(cls, name):
        print(f"The student {name} is in {random.choice(cls.houses)}")

def main():
    name = input("Enter the name of the student to be sorted: ")
    Hat.sort(name)

if __name__ == "__main__":
    main()