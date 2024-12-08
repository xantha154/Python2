from task_1 import Car, Formula1Car, RaceTrack
if __name__ == "__main__":
    car = Car(brand="Toyota", model="Camry", max_speed=180)
    f1_car = Formula1Car(team="Red Bull", engine_power=1000, aerodynamics_score=0.85)
    track = RaceTrack(name="Monaco", length=3, turns=19)
    try:
        car.drive(-50)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        invalid_f1_car = Formula1Car(team="Ferrari", engine_power=900, aerodynamics_score=1.5)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        track.lap_time(-150)
    except ValueError:
        print('Ошибка: неправильные данные')
