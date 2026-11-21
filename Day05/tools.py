from datetime import datetime
import random
import secrets
import string

def get_current_time():
    """Returns correct data and time"""
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

def roll_dice():
    """Returns a random number between 1 to 6"""
    return random.randint(1,6)
def generate_password(length=12):
    """Generate a secure random password"""
    characters = (string.ascii_letters + string.digits + string.punctuation)
    
    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password

def read_text_file(filename):
    """Reads a text file for given file"""
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error:File not found"



