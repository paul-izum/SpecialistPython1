# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here

tup1 = (3, 5, 4)
tup2 = (2, 4, -6, 5, 7, 8, 9, 10)
tup3 = (2, 4, -6, 11, 78, 13, 76, 3,5)

step_list = []
res_list = []

for tup in tup2:
    if tup in tup1:
        step_list.append(tup)

for tup in step_list:
    if tup in tup3:
        res_list.append(tup)

print( res_list)
print( len(res_list))
