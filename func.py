import json


def read_file():
    with open('func.json', 'r') as file:
        return json.load(file)

def write_file(students):
    with open('func.json', 'w') as file:
        json.dump(students, file, indent=4)

def add_student(students):
    number = int(input('Enter student ID number'))
    name = input('Enter student name')
    age = int(input('Enter student age'))
    city = input('Enter student city')

    new_student = {
        "name": name,
        "age": age,
        "city": city,
    }
    students.append(new_student)
    write_file(students)
    print(f'Successfully added:  {name}, {age}, {city}')

def view_student(students):
    print('\n List of students')
    for student in students:
        print(f'  {student['name']}, {student['age']}, {student['city']}')

students = read_file()
while True:
    print('1 to add student')
    print('2. To view list of students')
    print('3. Exit')

    choice = int(input('Enter your choice from 1-3'))

    if choice == 1:
        add_student(students)
    elif choice == 2:
        view_student(students)
    elif choice == 3:
        print('Program Terminated')
        break

