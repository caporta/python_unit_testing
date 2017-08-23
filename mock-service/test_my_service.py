import unittest

from .my_service import MyService
from .fake_single_sign_on_registry import FakeSingleSignOnRegistry


class MyServiceTest(unittest.TestCase):
    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request('do stuff', token=None)
        self.assertIn('please enter your login details', response)

    def test_valid_token(self):
        registry = FakeSingleSignOnRegistry()
        token = registry.register('valid credentials')
        my_service = MyService(registry)

        response = my_service.handle_request('do stuff', token)
        self.assertIn('hello world', response)
