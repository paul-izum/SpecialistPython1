# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
def meter_to_foot(*args):
    res = []
    for el in args:
        el = float(el) * 3.28
        res.append(el)
    return res

print(meter_to_foot(*distances))
