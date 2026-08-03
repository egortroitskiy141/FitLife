# Проект FitLife - MVP версия 1.0

# Вместо «магических цифр»
WATER_ML_PER_KG = 30
ML_IN_LITER = 1000


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# .strip() убирает пробелы до и после имени
user_name = input("Как вас зовут? ").strip()
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь
# преобразовать в число)
while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        break
    except ValueError:
        print("Ошибка: введите возраст целым числом, например 25.")

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
while True:
    try:
        user_weight = float(input("Какой у вас вес в кг? "))
        break
    except ValueError:
        print("Ошибка: введите вес числом, например 70.5.")
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height
# (тип float)
while True:
    try:
        user_height = float(input("Какой у вас рост в метрах? "))
        break
    except ValueError:
        print("Ошибка: введите рост числом, например 1.75.")

# 3. Логика расчетов (функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_needed = user_weight * WATER_ML_PER_KG / ML_IN_LITER

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например:
# "Привет, Иван!"
print(f"Привет, {user_name}!")
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Ваш возраст: {user_age} лет")
print(f"Ваш ИМТ: {bmi}")
print(f"Норма воды: {water_needed} л.")
print("Расчет окончен. Будьте здоровы!")
