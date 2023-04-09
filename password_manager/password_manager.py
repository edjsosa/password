import json
import getpass
from encryption import encrypt, decrypt


# File name to store passwords
PASSWORD_FILE = 'passwords.json'


def load_passwords():
    # Load passwords from file
    try:
        with open(PASSWORD_FILE, 'r') as f:
            passwords = json.load(f)

    except FileNotFoundError:
        passwords = {}

    return passwords


def save_passwords(passwords):

    # Save passwords to file
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)


def add_password(service, username, password):

    passwords = load_passwords()

    # Encrypt the password
    password = encrypt(password)

    # Add the password to the dictionary
    if service not in passwords:
        passwords[service] = {}

    passwords[service][username] = password

    save_passwords(passwords)


def get_password(service, username):

    passwords = load_passwords()

    # Get the password from the dictionary
    if service in passwords and username in passwords[service]:
        password = passwords[service][username]

        # Decrypt the password
        password = decrypt(password)
        return password

    else:
        return None


def remove_password(service, username):

    passwords = load_passwords()

    # Remove the password from the dictionary
    if service in passwords and username in passwords[service]:

        del passwords[service][username]
        save_passwords(passwords)


def list_services():

    services = sorted(load_passwords().keys())

    if len(services) > 0:

        print('Services:')
        for service in services:
            print(service)

    else:
        print('Services not found.')


def prompt_service():
    return input('Enter the name of the service: ')


def prompt_user():
    return input('Enter your username: ')


def prompt_password():
    return getpass.getpass('Enter the password: ')


def main():

    choice = '0'
    while choice != '5':

        print('\nWelcome to your password manager!')
        print('1. Add password')
        print('2. Get password')
        print('3. Remove password')
        print('4. List services')
        print('5. Quit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            add_password(prompt_service(), prompt_user(), prompt_password())
            print('Password added successfully.')

        elif choice == '2':
            password = get_password(prompt_service(), prompt_user())

            if password:
                print('Your password is:', password)
            else:
                print('Password not found.')

        elif choice == '3':
            remove_password(prompt_service(), prompt_user())
            print('Password removed successfully.')

        elif choice == '4':
            list_services()

        elif choice == '5':
            break

        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
