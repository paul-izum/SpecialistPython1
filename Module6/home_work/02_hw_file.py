# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

s = 0
with open("data/info.txt", "r") as f:
    for line in f:
        if line.rstrip().isdigit():
            s += int(line)
       # print(line.rstrip().isdigit())
print(s)
