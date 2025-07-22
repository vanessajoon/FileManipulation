import json

with open('project1.json', 'r') as file:
    student = json.load(file)

while True:
    name = input('Enter student name')
    age = int(input('Enter student age'))
    city = input('Enter student city')

    updated_student = {
        "name": name,
        "age": age,
        "city": city
    }
    student.append(updated_student)

    with open('project1.json', 'w') as file:
        json.dump(student, file, indent=4)
    print(f'Student Successfully added: {name}, {age}, {city}')

    print('1 to view ')
    print('2 to to add another student  ')
    print('3 to exist')
    choice = int(input('Enter your choice'))

    if choice == 1:
        for students in student:
            print(f'{students['name']}, {students['age']}, {students['city']}')
        break
    elif choice == 2:
        continue
    elif choice == 3:
        break