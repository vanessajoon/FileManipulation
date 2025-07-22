#working with json files
#JSON - javascipt object notion
import json

#to read a json file
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data['name'])

#to write in a json file
first_person = {
    'name': 'Damilola',
    'age': 19,
    'city': 'Lagos'
}
with open('data.json', 'w') as file:
    json.dump([first_person], file, indent=4)

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

new_person = {
    'name': 'Joy',
    'age': 19,
    'city': 'Lagos'
}
data.append(new_person)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

