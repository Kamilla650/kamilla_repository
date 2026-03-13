# ============================================
# ДОМАШНЕЕ ЗАДАНИЕ: СЛОВАРИ И ГЕНЕРАТОРЫ
# ============================================

# ===== ЗАДАЧА 1: Телефонная книга =====
print("\n" + "=" * 50)
print("ЗАДАЧА 1: Телефонная книга")
print("=" * 50)

phone_book = []  # Список для хранения контактов


def add_contact(name, phone, email, group):
    """Добавление нового контакта"""
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "group": group
    }
    phone_book.append(contact)
    print(f"✓ Контакт {name} добавлен")


def search_by_name(name):
    """Поиск контакта по имени"""
    results = []
    for contact in phone_book:
        if contact["name"].lower() == name.lower():
            results.append(contact)
    return results


def show_group(group):
    """Показать все контакты из группы"""
    results = []
    for contact in phone_book:
        if contact["group"].lower() == group.lower():
            results.append(contact)
    return results


def delete_contact(name):
    """Удаление контакта по имени"""
    global phone_book
    before = len(phone_book)
    phone_book = [c for c in phone_book if c["name"].lower() != name.lower()]
    after = len(phone_book)
    if before > after:
        print(f"✓ Контакт {name} удален")
    else:
        print(f"✗ Контакт {name} не найден")


# ТЕСТИРУЕМ ЗАДАЧУ 1
print("\n--- Тестирование ---")
add_contact("Иван", "123-45-67", "ivan@mail.ru", "друзья")
add_contact("Мария", "234-56-78", "maria@mail.ru", "работа")
add_contact("Петр", "345-67-89", "petr@mail.ru", "друзья")

print("\nПоиск контакта 'Иван':")
found = search_by_name("Иван")
for contact in found:
    print(f"  Найден: {contact}")

print("\nВсе контакты из группы 'друзья':")
friends = show_group("друзья")
for contact in friends:
    print(f"  {contact['name']} - {contact['phone']}")

print("\nУдаляем Петра:")
delete_contact("Петр")

print("\nТекущая телефонная книга:")
for contact in phone_book:
    print(f"  {contact}")

# ===== ЗАДАЧА 2: Анализ успеваемости =====
print("\n" + "=" * 50)
print("ЗАДАЧА 2: Анализ успеваемости")
print("=" * 50)

# Исходные данные
students = [
    {"name": "Иван", "grades": [4, 5, 3, 5, 4]},
    {"name": "Анна", "grades": [5, 5, 5, 4, 5]},
    {"name": "Петр", "grades": [3, 3, 4, 3, 4]}
]

# Создаем словарь с анализом
result = {}

for student in students:
    name = student["name"]
    grades = student["grades"]

    # Вычисления
    avg = sum(grades) / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)
    fives = grades.count(5)

    # Сохраняем результат
    result[name] = {
        "средний балл": round(avg, 2),
        "максимальная оценка": max_grade,
        "минимальная оценка": min_grade,
        "количество пятерок": fives
    }

# Выводим результаты
print("\nРезультаты анализа:")
for name, stats in result.items():
    print(f"\n{name}:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

# ===== ЗАДАЧА 3: Инвентаризация магазина =====
print("\n" + "=" * 50)
print("ЗАДАЧА 3: Инвентаризация магазина")
print("=" * 50)

# Исходные данные
inventory = {
    "фрукты": {
        "яблоки": {"price": 80, "quantity": 50},
        "бананы": {"price": 60, "quantity": 30}
    },
    "овощи": {
        "морковь": {"price": 40, "quantity": 20},
        "картофель": {"price": 30, "quantity": 100}
    }
}


def show_category(category):
    """Показать все товары в категории"""
    if category in inventory:
        print(f"\nТовары в категории '{category}':")
        for product, info in inventory[category].items():
            print(f"  {product}: {info['price']} руб, {info['quantity']} шт")
    else:
        print(f"Категория '{category}' не найдена")


def buy_product(category, product, quantity):
    """Купить товар (уменьшить количество)"""
    if category in inventory:
        if product in inventory[category]:
            if inventory[category][product]["quantity"] >= quantity:
                inventory[category][product]["quantity"] -= quantity
                print(f"✓ Куплено {quantity} шт {product}")
                print(f"  Осталось: {inventory[category][product]['quantity']} шт")
            else:
                print(f"✗ Недостаточно товара. В наличии: {inventory[category][product]['quantity']} шт")
        else:
            print(f"Товар '{product}' не найден в категории '{category}'")
    else:
        print(f"Категория '{category}' не найдена")

def total_value():
    """Посчитать общую стоимость всех товаров"""
    total = 0
    for category in inventory.values():
        for product in category.values():
            total += product["price"] * product["quantity"]
    return total

# ТЕСТИРУЕМ ЗАДАЧУ 3
print("\n--- Тестирование ---")

show_category("фрукты")

print("\nПокупка 10 яблок:")
buy_product("фрукты", "яблоки", 10)

print("\nПроверяем остаток:")
show_category("фрукты")

print(f"\nОбщая стоимость всех товаров: {total_value()} руб")

# ===== ЗАДАЧА 4: Генератор словарей =====
print("\n" + "=" * 50)
print("ЗАДАЧА 4: Генератор словарей")
print("=" * 50)

# 1. Из списка слов создайте словарь (слово: длина_слова)
print("\n1. Словарь слов и их длины:")
words = ["яблоко", "груша", "банан", "апельсин"]
word_dict = {word: len(word) for word in words}
print(f"   Слова: {words}")
print(f"   Результат: {word_dict}")

# 2. Из двух списков создайте словарь
print("\n2. Словарь из двух списков:")
keys = ["имя", "возраст", "город"]
values = ["Анна", 25, "Москва"]
dict_from_lists = {keys[i]: values[i] for i in range(len(keys))}
print(f"   Ключи: {keys}")
print(f"   Значения: {values}")
print(f"   Результат: {dict_from_lists}")

# 3. Из текста создайте словарь частоты символов
print("\n3. Частота символов в тексте:")
text = "пример текста для анализа"
freq_dict = {char: text.count(char) for char in set(text)}
print(f"   Текст: '{text}'")
print(f"   Результат: {freq_dict}")

# 4. Инвертируйте полученный словарь частоты
print("\n4. Инвертированный словарь частоты:")
inverted_dict = {}
for char, count in freq_dict.items():
    if count not in inverted_dict:
        inverted_dict[count] = []
    inverted_dict[count].append(char)
print(f"   Исходный: {freq_dict}")
print(f"   Инвертированный: {inverted_dict}")

