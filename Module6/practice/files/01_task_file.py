# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

path = "data/limericks.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в тойже папке что и текущий файл

# Открываем файл на чтение
f = open(path, "r", encoding = "utf-8")
# В переменную line считываем строку за стройкой из файла(f)
#1
for line in f:
    line = line.rstrip()
    print(line)
f.close()
#2
f = open(path, "r", encoding = "utf-8")
sym_count = 0
for line in f:
    sym_count_str = len(line.replace(" ", "").replace("\n", "").replace("\t",""))
    sym_count += sym_count_str
print(sym_count)
f.close()
#3
f = open(path, "r", encoding = "utf-8")
poem_count = 0
for line in f:
    if len(line.rstrip()) == 0:
        poem_count += 1
print(poem_count)
f.close()

# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.
