# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    number = str(number)
    i = 0
    j = len(number) - 1
    palindrome = True
    while i < j:
        if number[i] != number[j]:
            palindrome = False
            return "NO"
        i += 1
        j -= 1
    if palindrome == True:
        return "YES"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
