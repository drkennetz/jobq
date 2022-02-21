"""
Utilities warehouse
"""

from getpass import getpass
import bcrypt

def enter_password():
    """ Enters a password for server security
    Args: None
    Returns:
        [empty string, hashed_password, or retries function if mismatch]
    """
    password1 = getpass('Enter Password [enter for None]:')
    password2 = getpass('Enter a second time [must match]:')
    if password1 != password2:
        print("Passwords did not match... Trying again (ctrl+c to exit)")
        return enter_password()
    elif (password1 == password2) and password1 != '':
        return bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    else:
        return password1

def validate_password(plain_text_password, hashed_password):
    """ Validates a plain text password
    Args:
        plain_text_password (str): the password to validate
        hashed_password (bytes): the bcrypt hashed password
    Returns:
        Boolean
    """
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

def decode_dict(zmqdict):
    """ Decodes a dict sent by zmq """
    return dict((k.decode('utf-8'), v.decode('utf-8')) for k,v in zmqdict.items())
