from phonebook import Phonebook


def test_add_and_lookup_entry():
    phonebook = Phonebook()
    phonebook.add('Bob', '123')
    assert '123' == phonebook.lookup('Bob')


def test_phonebook_gives_access_to_names():
    phonebook = Phonebook()
    phonebook.add('Alice', '12345')
    assert 'Alice' in phonebook.names()


def test_phonebook_gives_access_to_numbers():
    phonebook = Phonebook()
    phonebook.add('Alice', '12345')
    assert '12345' in phonebook.numbers()
