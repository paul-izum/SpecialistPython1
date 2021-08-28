# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    number = str(number)
    return number == number[::-1]

def palindrome_cnt(a,b):
    cnt = 0
    for numb in range (a,b+1):
        if palindrome(numb):
            cnt += 1
            #print(numb)
    return cnt


print(palindrome_cnt(100,120))
