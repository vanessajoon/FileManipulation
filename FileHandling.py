# #To read a file
# file = open('example.txt', 'r') #r means read mode
# content = file.read()
# print(content)
# file.close() #always close the file!
#
# #to write in a file
# file = open('example.text', 'w')
# file.write('Hello Python!\n')
# file.close()
#
# #to append to a file
# file = open('example.txt', 'a')
# file.write('I am learning alot\n')
# file.close()
#
# #Best practice use with open
# #with open function automatically closes the file after use
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
#
# with open('example,txt', 'a') as file:
#     file.write('This is line 1\n')
#     file.write('This is line 2 \n')
#     file.write('This is line 3 \n')


with open('example.txt', 'w') as file:
    file.write('My name is vanessa\n')
    file.write('I am 19 years old\n')
    file.write('And I am a Software Engineer\n')
    file.write('Please hire me\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)