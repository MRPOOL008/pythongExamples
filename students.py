import csv

def main():

    #Get the inputs from user
    name = input("Enter your name: ")
    home = input("Where are you from? ")

    #insert to files
    with open("students.csv", "a", newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "home"])
        writer.writerow({"name" : name, "home" : home})

    #select from files
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    print()
    for student in sorted(students, key = lambda student: student["name"]):
        print(f"Hi {student['name']} from {student['home']}!\n")
            


if __name__ == "__main__":
    main()