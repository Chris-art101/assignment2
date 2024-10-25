# lists
employees = ['Peter', 'John', 'Smith', 'Esther']
print(employees)
print(employees[1])
print(employees[1:4])
employees[3] = 'William'
print(employees)
employees.append('Koi')
print(employees)
employees.insert(0,'Juliana')
print(employees)
employees.extend(['Paul', 'Ann', 'Susan'])
print(employees)
# tuples (you cannot reassign values like in the list because they are retained as permanent)
languages = ('Python', 'Java', 'Kotlin')
print(languages)
print(languages[1])
print(languages[1:3])

# sets{identified using calibraces}
students = {'Andrew', 'Winnie', 'Alex','Paul'}
print(students)
if 'Andrew' in students:
    print('Andrew')
if 'Andrew' in students:
    print('Winnie')
if 'Alex' in students:
    print('Alex')
if 'Paul' in students:
    print('Paul')
if 'Susan' in students:
    print('Susan')
else:
    print('not present')
students.add('Charles')
print(students)
students.update(['Reubben'])
print(students)
students.remove('Charles')
print(students)

# dictionary

pupil = {
    'first_name':'Chris',
    'last_name': 'Njue',
    'email': "njue@gmail.com",
    'gender': 'Female',
    'birthyear': '1999'
}
print(pupil)
print(pupil['email'])
pupil['skintone'] = 'brown'
print(pupil)

if 'skintone' in pupil:
    print('Yes it is present')
else:
    print('Not present')

immigrant = {
    'first_name':'Myles',
    'last_name': 'White',
    'citizenship': 'Briton',
    'gender': 'Male',
}
print(immigrant)
print(immigrant['gender'])
immigrant['citizenship'] = 'briton'
print(immigrant)

if 'citizenship' in immigrant:
    print('Yes it is present')
else:
    print('Not present')



