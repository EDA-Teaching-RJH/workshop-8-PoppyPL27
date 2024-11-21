def main():
    add_student("Amy Pond", 23, 'A')
    add_student("Rory Williams", 24, 'C')
    add_student("The Doctor", 9000, "A*")
    display_students()
    find_student("Amy Pond")

def add_student(name, age, grade):
    file = open("students.txt", "a")
    file.write(f"{name},{str(age)},{str(grade)}\n")
    file.close()

def  display_students():
    file = open("students.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()

def  find_student(name):
    file = open("students.txt", "r")
    lines = file.readlines()
    for line in lines:
        row = line.rstrip().split(",")
        if (row[0] == name):
            print("file of "+name)
            print(line)
    file.close()

if __name__ == "__main__":
    main()