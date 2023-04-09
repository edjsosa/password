import pytest

from encryption import encrypt
from password_manager import add_password, load_passwords, save_passwords, get_password

def test_add_password():
    service = 'Gmail'
    username = 'john.doe@gmail.com'
    password = 'secret'

    # Call the add_password function
    add_password(service, username, password)

    # Check that the password was added to the dictionary
    passwords = load_passwords()
    assert service in passwords
    assert username in passwords[service]
    assert passwords[service][username] == encrypt(password)

    # Remove the test password from the dictionary
    del passwords[service][username]
    if not passwords[service]:
        del passwords[service]
    save_passwords(passwords)


def test_get_password():
    # Add a password to the file
    add_password("gmail", "testuser", "secretpassword")

    # Test that the correct password is returned for the correct service and username
    password = get_password("gmail", "testuser")
    assert password == "secretpassword"

    # Test that None is returned if the service or username is not found
    password = get_password("yahoo", "testuser")
    assert password is None

    password = get_password("gmail", "nonexistentuser")
    assert password is None

    # Test that the returned password is decrypted
    add_password("netflix", "johndoe", "netflixrocks")
    password = get_password("netflix", "johndoe")
    assert password == "netflixrocks"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])