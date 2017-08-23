class FakeSingleSignOnRegistry:
    def __init__(self):
        self.tokens = set()

    def register(self, credentials):
        if are_valid(credentials):
            token = SSOToken()
            self.tokens.add(token)
            return token

    def is_valid(self, token):
        return token in self.tokens

    def end_session(self, token):
        self.tokens.remove(token)


class SSOToken:
    pass


def are_valid(credentials):
    # check creds
    return True
