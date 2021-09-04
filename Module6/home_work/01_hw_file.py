# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="data/log.txt"):
    with open(file, "a") as f:
        # print(f"{text}")
        f.write(f"{text}\n")


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
