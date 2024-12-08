class Car:
    def __init__(self, brand: str, model: str, max_speed: int):
        """
        Инициализирует объект Car.

        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param max_speed: Максимальная скорость автомобиля в км/ч.
        :raises ValueError: Если max_speed <= 0.
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть больше 0.")

        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    def drive(self, distance: int) -> float:
        """
        Расчитывает примерное время, необходимое для проезда указанной дистанции.

        :param distance: Дистанция в километрах.
        :return: Время в часах.
        :raises ValueError: Если distance <= 0.

        >>> car = Car("Toyota", "Camry", 180)
        >>> car.drive(360)
        2.0
        """
        if distance <= 0:
            raise ValueError("Дистанция должна быть больше 0.")
        return distance / self.max_speed

    def honk(self, sound: str = "Beep") -> str:
        """
        Генерирует звук сигнала автомобиля.

        :param sound: Пользовательский звук сигнала (по умолчанию "Beep").
        :return: Звук сигнала.

        >>> car = Car("Ford", "Focus", 200)
        >>> car.honk()
        'Beep'
        >>> car.honk("Honk-Honk")
        'Honk-Honk'
        """
        return sound


class Formula1Car:
    def __init__(self, team: str, engine_power: int, aerodynamics_score: float):
        """
        Инициализирует объект Formula1Car.

        :param team: Название команды.
        :param engine_power: Мощность двигателя в л.с.
        :param aerodynamics_score: Аэродинамический коэффициент (0.0 < aerodynamics_score <= 1.0).
        :raises ValueError: Если aerodynamics_score выходит за допустимые границы.
        """
        if not (0.0 < aerodynamics_score <= 1.0):
            raise ValueError("Аэродинамический коэффициент должен быть в пределах (0.0, 1.0].")

        self.team = team
        self.engine_power = engine_power
        self.aerodynamics_score = aerodynamics_score

    def calculate_speed(self) -> float:
        """
        Рассчитывает максимальную скорость болида на основе мощности двигателя и аэродинамики.

        :return: Максимальная скорость в км/ч.

        >>> f1_car = Formula1Car("Red Bull", 1000, 0.85)
        >>> round(f1_car.calculate_speed(), 2)
        850.0
        """
        return self.engine_power * self.aerodynamics_score

    def pit_stop(self, action: str) -> str:
        """
        Осуществляет действия на пит-стопе.

        :param action: Действие, выполняемое на пит-стопе (например, "смена шин").
        :return: Сообщение о выполненном действии.

        >>> f1_car = Formula1Car("Ferrari", 950, 0.8)
        >>> f1_car.pit_stop("смена шин")
        'Пит-стоп выполнен: смена шин'
        """
        return f"Пит-стоп выполнен: {action}"
class RaceTrack:
    def __init__(self, name: str, length: int, turns: int):
        """
        Инициализирует объект RaceTrack.

        :param name: Название трассы.
        :param length: Длина трассы в километрах.
        :param turns: Количество поворотов.
        :raises ValueError: Если длина трассы <= 0 или количество поворотов < 0.
        """
        if length <= 0:
            raise ValueError("Длина трассы должна быть больше 0.")
        if turns < 0:
            raise ValueError("Количество поворотов не может быть отрицательным.")

        self.name = name
        self.length = length
        self.turns = turns

    def lap_time(self, car_speed: float) -> float:
        """
        Рассчитывает примерное время прохождения круга.

        :param car_speed: Средняя скорость автомобиля в км/ч.
        :return: Время круга в минутах.
        :raises ValueError: Если car_speed <= 0.

        >>> track = RaceTrack("Silverstone", 5, 18)
        >>> round(track.lap_time(200), 2)
        1.5
        """
        if car_speed <= 0:
            raise ValueError("Скорость автомобиля должна быть больше 0.")
        return (self.length / car_speed) * 60

    def race_info(self, laps: int = 1) -> str:
        """
        Возвращает информацию о гонке.

        :param laps: Количество кругов (по умолчанию 1).
        :return: Информация о гонке.

        >>> track = RaceTrack("Monaco", 3, 19)
        >>> track.race_info(3)
        'Гонка: трасса Monaco, длина 3 км, поворотов 19, кругов 3.'
        """
        return f"Гонка: трасса {self.name}, длина {self.length} км, поворотов {self.turns}, кругов {laps}."