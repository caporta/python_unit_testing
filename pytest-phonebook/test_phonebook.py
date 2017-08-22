import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    phonebook = Phonebook(tmpdir)
    return phonebook


def test_add_and_lookup_entry(phonebook):
    phonebook.add('Bob', '123')
    assert '123' == phonebook.lookup('Bob')


def test_phonebook_gives_access_to_names(phonebook):
    phonebook.add('Alice', '12345')
    assert 'Alice' in phonebook.names()


def test_phonebook_gives_access_to_numbers(phonebook):
    phonebook.add('Alice', '12345')
    assert '12345' in phonebook.numbers()


def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('missing')
