from tennis import tennis_score

import pytest


SCORES = (
    ('expected_score', 'player_one_score', 'player_two_score'),
    [
        ('Love-All', 0, 0),
        ('Fifteen-All', 1, 1),
        ('Thirty-All', 2, 2),
    ],
)


@pytest.mark.parametrize(*SCORES)
def test_early_game_scores_equal(expected_score, player_one_score, player_two_score):
    assert expected_score == tennis_score(player_one_score, player_two_score)


def test_early_game_scores_equal_ordinary():
    assert 'Love-All' == tennis_score(0, 0)
    assert 'Fifteen-All' == tennis_score(1, 1)
    assert 'Thirty-All' == tennis_score(2, 2)
