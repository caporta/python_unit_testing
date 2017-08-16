from phonebook import Phonebook

def test_add_and_lookup_entry():
    phonebook = Phonebook()
    phonebook.add('Bob', '123')
    assert '123' == phonebook.lookup('Bob')
