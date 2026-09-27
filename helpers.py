import random
import string
import time


def generate_email():
    prefix = "Vitaly_Shitov_54_"
    timestamp = str(int(time.time()))[-3:]
    domain = "ya.ru"
    return f"{prefix}{timestamp}@{domain}"


def generate_password(length=10):
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
