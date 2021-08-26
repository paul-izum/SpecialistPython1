# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
max_emp = staff[0]
for emp in staff:
    if emp["salary"] > max_emp["salary"]:
        max_emp = emp

print(max_emp["name"], max_emp["surname"])

# TODO: your code here

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
min_emp = staff[0]
for emp in staff:
    if emp["salary"] < min_emp["salary"]:
        min_emp = emp
        #print(min_emp)

print(min_emp["name"], min_emp["surname"])
# TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")


# TODO: your code here

s_sal = 0

for emp in staff:
    s_sal = s_sal + emp["salary"]

print(s_sal/len(staff))



print("Количество однофамильцев в организации")



# TODO: your code here


namer = 0

for emp1 in staff:
    for emp2 in staff:
        if emp1 != emp2:
            if emp1.get("surname") == emp2.get("surname"):
                namer +=1
                break
print(namer, "\n")


# surnames = [emp['surname'] for emp in staff]
# namesakes = [sn for sn in surnames if surnames.count(sn) > 1]
# print(len(namesakes))
# print()


print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")



# TODO: your code here
for a in range(len(staff)):
    i = 0
    while i < len(staff)-1:
        if staff[i].get("salary") > staff[i+1].get("salary"):
            staff[i], staff[i+1] = staff[i+1], staff[i]
        i += 1

for a in staff:
    print(f"{a.get('name')}, {a.get('surname')}, {a.get('salary')}")
    
    
