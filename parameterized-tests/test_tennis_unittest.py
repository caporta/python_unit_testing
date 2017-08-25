import unittest

from .tennis import tennis_score

TEST_CASE_DATA = {
    'even_scores': [
        ('Love-All', 0, 0),
        ('Fifteen-All', 1, 1),
        ('Thirty-All', 2, 2),
    ],
    'early_games_with_uneven_scores': [
        ('Love-Fifteen', 0, 1),
        ('Fifteen-Love', 1, 0),
        ('Love-Thirty', 0, 2),
        ('Forty-Thirty', 3, 2),
    ],
}


def tennis_test_template(*args):
    return lambda self: self.assert_tennis_score(*args)


class TennisTest(unittest.TestCase):
    def assert_tennis_score(self, expected_score, player_one_score, player_two_score):
        self.assertEqual(expected_score, tennis_score(player_one_score, player_two_score))


for behavior, test_cases in TEST_CASE_DATA.items():
    for tennis_test_case_data in test_cases:
        expected_output, player_one_score, player_two_score = tennis_test_case_data
        test_name = 'test_{0}_{1}_{2}'.format(behavior, player_one_score, player_two_score)
        tennis_test_case = tennis_test_template(*tennis_test_case_data)
        setattr(TennisTest, test_name, tennis_test_case)
