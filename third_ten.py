students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

all_people = students.union(employees)
print("Все люди (первый способ):", all_people)

all_people = students | employees
print("Все люди :", all_people)

###
both = students.intersection(employees)
print("Те, кто учится и работает (первый способ):", both)

both = students & employees
print("Те, кто учится и работает (второй способ):", both)

###
both = employees - students
print("Те, кто учится != работает:", both)

both = employees.difference(students)
print("Те, кто учится != работает:", both)

###
either_or = students.symmetric_difference(employees)
print("Те, кто либо учится, либо работает, но не одновременно (первый способ):", either_or)

either_or = students ^ employees
print("Те, кто либо учится, либо работает, но не одновременно (второй способ):", either_or)
