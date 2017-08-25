import unittest
from unittest.mock import Mock, patch

from alarm import Alarm
from sensor import Sensor


class AlarmTest(unittest.TestCase):
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_low_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(15))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_normal_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(20))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_normal_pressure_with_unittest_mock(self):
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    @patch('alarm.Sensor')
    def test_high_pressure_with_monkeypatch(self, test_sensor_class):
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 22
            test_sensor_class.return_value = test_sensor_instance
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)

class TestSensor:
    def __init__(self, pressure):
        self._pressure = pressure

    def sample_pressure(self):
        return self.pressure

    @property
    def pressure(self):
        return self._pressure
