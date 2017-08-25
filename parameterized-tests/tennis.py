SCORE_NAMES = ['Love', 'Fifteen', 'Thirty', 'Forty']


def tennis_score(player_one_score, player_two_score):
    if player_one_score == player_two_score:
        return "{0}-All".format(SCORE_NAMES[player_one_score])
    return '{0}-{1}'.format(SCORE_NAMES[player_one_score], SCORE_NAMES[player_two_score])
