employee = {
    'name': 'Bharat',
    'age': 25,
}

print(employee)


employee['test'] = 26
print(employee)

employee.pop('test')
print(employee)

for key in employee:
    print(key, employee[key])

for key, value in employee.items():
    print(key, value)

for key in employee.keys():
    print(key)

for value in employee.values():
    print(value)