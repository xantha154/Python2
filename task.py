# TODO: описать базовый класс
class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.
    """
    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует объект транспортного средства.

        :param brand: Бренд транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.

        :return: Информация о транспортном средстве.
        """
        return f"Vehicle: {self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.

        :return: Строка с именем класса и атрибутами.
        """
        return f"Vehicle(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"

    def get_description(self) -> str:
        """
        Возвращает описание транспортного средства.

        :return: Описание транспортного средства.
        """
        return f"{self.brand} {self.model}, manufactured in {self.year}."


class Car(Vehicle):
    """
    Дочерний класс, представляющий легковой автомобиль.
    """
    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int) -> None:
        """
        Инициализирует объект легкового автомобиля, расширяя базовый класс Vehicle.

        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param passenger_capacity: Количество пассажиров, которых может перевозить автомобиль.
        """
        super().__init__(brand, model, year)
        self.passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        """
        Переопределяет метод str для отображения дополнительных данных.

        :return: Информация о легковом автомобиле.
        """
        return f"Car: {self.brand} {self.model} ({self.year}), Capacity: {self.passenger_capacity} passengers"

    def get_description(self) -> str:
        """
        Переопределяет метод для описания легкового автомобиля.



        :return: Описание легкового автомобиля.
        """
        return f"{super().get_description()} It can carry up to {self.passenger_capacity} passengers."


class Truck(Vehicle):
    """
    Дочерний класс, представляющий грузовой автомобиль.
    """
    def __init__(self, brand: str, model: str, year: int, max_payload: float) -> None:
        """
        Инициализирует объект грузового автомобиля, расширяя базовый класс Vehicle.

        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param max_payload: Максимальная грузоподъемность автомобиля (в тоннах).
        """
        super().__init__(brand, model, year)
        self.__max_payload = max_payload  # Инкапсулируем, чтобы ограничить прямое изменение

    def __str__(self) -> str:
        """
        Переопределяет метод str для отображения дополнительных данных.

        :return: Информация о грузовом автомобиле.
        """
        return f"Truck: {self.brand} {self.model} ({self.year}), Max Payload: {self.__max_payload} tons"

    def get_description(self) -> str:
        """
        Переопределяет метод для описания грузового автомобиля.



        :return: Описание грузового автомобиля.
        """
        return f"{super().get_description()} It can carry up to {self.__max_payload} tons."

    def get_payload(self) -> float:
        """
        Возвращает максимальную грузоподъемность грузовика.

        :return: Максимальная грузоподъемность в тоннах.
        """
        return self.__max_payload


# Пример использования
if __name__ == "__main__":
    car = Car("Lada", "Vesta", 2022, 5)
    truck = Truck("Volvo", "FH16", 2021, 20)

    print(car)  # Car: Lada Vesta (2022), Capacity: 5 passengers
    print(truck)  # Truck: Volvo FH16 (2021), Max Payload: 20 tons

    print(car.get_description())
    print(truck.get_description())
# TODO: описать дочерний класс
