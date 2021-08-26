# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    first_part = ticket_number//100000 + (ticket_number//10000%10) + (ticket_number//1000)%10
    second_part = (ticket_number//100)%10 + (ticket_number//10)%10 + ticket_number%10
    if first_part == second_part:
        return True
    return False

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
