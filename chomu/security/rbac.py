import getpass

USERS = {
    'admin': 'changeme',  # Replace with hashed passwords in production
}

def check_user(username, password):
    return USERS.get(username) == password

def require_auth():
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    if not check_user(username, password):
        print('Authentication failed.')
        return False
    return True
