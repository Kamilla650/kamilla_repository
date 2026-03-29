class SpaceSection:
    def __init__(self, name, oxygen, temperature, access_code, pressure):
        self.name = name
        self.__oxygen_level = oxygen
        self.__temperature = temperature
        self.__access_code = access_code
        self.__captain_password = "admin123"  # секретный пароль капитана
        self.__pressure = pressure  # новое приватное поле давления

    # Геттеры
    def get_oxygen(self):
        return f"Уровень кислорода в {self.name}: {self.__oxygen_level}%"

    def get_temperature(self):
        return f"Температура в {self.name}: {self.__temperature}°C"

    def get_access_code(self, password):
        if password == self.__captain_password:
            return f"Код доступа к {self.name}: {self.__access_code}"
        else:
            return "🚫 Доступ запрещен! Неверный пароль капитана!"

    def get_pressure(self):
        return f"Давление в {self.name}: {self.__pressure} атм"

    # Сеттеры
    def set_oxygen(self, level):
        if 0 <= level <= 100:
            self.__oxygen_level = level
            print(f"✅ Уровень кислорода в {self.name} изменен на {level}%")
        else:
            print("❌ Ошибка! Уровень кислорода должен быть от 0 до 100")

    def set_temperature(self, temp):
        if -50 <= temp <= 50:
            self.__temperature = temp
            print(f"✅ Температура в {self.name} изменена на {temp}°C")
        else:
            print("❌ Ошибка! Температура должна быть от -50 до +50")

    def set_access_code(self, old_code, new_code):
        if old_code == self.__access_code:
            if len(str(new_code)) == 4 and str(new_code).isdigit():
                self.__access_code = str(new_code)
                print(f"✅ Код доступа к {self.name} успешно изменен")
            else:
                print("❌ Новый код должен состоять из 4 цифр!")
        else:
            print("❌ Неверный текущий код доступа!")

    def set_pressure(self, pressure):
        # нормальное давление считаем 0.5–2.0 атм
        if 0.5 <= pressure <= 2.0:
            self.__pressure = pressure
            print(f"✅ Давление в {self.name} изменено на {pressure} атм")
        else:
            print("❌ Ошибка! Давление должно быть в диапазоне от 0.5 до 2.0 атм")

    # Задание 4 (emergency_report) можно не трогать или вообще удалить,
    # если вам сказали его не делать.
    def emergency_report(self, password):
        if password == self.__captain_password:
            print("\n" + "=" * 40)
            print(f"🚨 АВАРИЙНЫЙ ОТЧЕТ: {self.name}")
            print(f"Кислород: {self.__oxygen_level}%")
            print(f"Температура: {self.__temperature}°C")
            print(f"Давление: {self.__pressure} атм")
            print(f"Код доступа: {self.__access_code}")
            print("=" * 40)
        else:
            print("Только капитан может просматривать аварийные отчеты!")


# Бонус: класс космического корабля БЕЗ автоматической проверки (только вывод)
class Spaceship:
    def __init__(self):
        # Создаем три отсека
        self.sections = [
            SpaceSection("Жилой отсек", 75, 22, "1234", 1.0),
            SpaceSection("Двигательный отсек", 85, 50, "5678", 1.5),
            SpaceSection("Научный отсек", 70, 18, "9012", 0.9),
        ]

    def check_all_systems(self):
        print("\n" + "=" * 50)
        print(" ПРОВЕРКА ВСЕХ СИСТЕМ КОРАБЛЯ ")
        print("=" * 50)
        for section in self.sections:
            print(section.get_oxygen())
            print(section.get_temperature())
            print(section.get_pressure())
            print("-" * 30)


# Диалоговая система для взаимодействия с пользователем
def run_dialog():
    section = SpaceSection("Командный отсек", 80, 21, "4321", 1.0)

    while True:
        print("\nЧто вы хотите сделать?")
        print("1 - Показать параметры")
        print("2 - Изменить кислород")
        print("3 - Изменить температуру")
        print("4 - Изменить давление")
        print("5 - Показать код доступа (нужен пароль капитана)")
        print("6 - Аварийный отчёт (если оставили метод)")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            print(section.get_oxygen())
            print(section.get_temperature())
            print(section.get_pressure())

        elif choice == "2":
            try:
                level = float(input("Новый уровень кислорода (0-100): "))
                section.set_oxygen(level)
            except ValueError:
                print("Введите число!")

        elif choice == "3":
            try:
                temp = float(input("Новая температура (-50..50): "))
                section.set_temperature(temp)
            except ValueError:
                print("Введите число!")

        elif choice == "4":
            try:
                pressure = float(input("Новое давление (0.5..2.0): "))
                section.set_pressure(pressure)
            except ValueError:
                print("Введите число!")

        elif choice == "5":
            pwd = input("Введите пароль капитана: ")
            print(section.get_access_code(pwd))

        elif choice == "6":
            pwd = input("Введите пароль капитана для аварийного отчёта: ")
            section.emergency_report(pwd)

        elif choice == "0":
            print("Выход из системы.")
            break
        else:
            print("Неизвестная команда, попробуйте еще раз.")

    if __name__ == "__main__":
        print("ЗАПУСК СИСТЕМЫ КОСМИЧЕСКОГО КОРАБЛЯ")
        ship = Spaceship()
        ship.check_all_systems()
        run_dialog()