import random
import string
from pathlib import Path


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_password():
    upper = random.choice(string.ascii_uppercase)
    lower = random.choices(string.ascii_lowercase, k=6)
    digits = random.choices(string.digits, k=3)
    special = random.choice("!@#$%^&*")
    chars = list(''.join(lower) + upper + ''.join(digits) + special)
    random.shuffle(chars)
    return ''.join(chars)


def generate_user_data():
    name = generate_random_string(8)
    return {
        "username": name,
        "email": f"{name}@gmail.com",
        "password": generate_password()
    }


def get_asset_path(filename):
    return str(Path(__file__).parent / "assets" / filename)