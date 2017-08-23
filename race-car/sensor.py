import random


class Sensor:
    _OFFSET = 16

    def sample_pressure(self):
        pressure_telemetry_value = Sensor.sample_actual_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_actual_pressure():
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value
