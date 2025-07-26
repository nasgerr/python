class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._verify_model(model)
        self._verify(speed)
        self._verify(top)
        self._verify(mass)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top
    def _verify_model(self, value):
        if type(value) != str:
            raise TypeError
    def _verify(self, value):
        if type(value) not in (int, float):
            raise TypeError
class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._verify_chairs(chairs)
        self._chairs = chairs
    def _verify_chairs(self, value):
        if type(value) != int:
            raise TypeError
class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._verify_weapons(weapons)
        self._weapons = weapons
    def _verify_weapons(self, value):
        if type(value) != dict:
            raise TypeError
