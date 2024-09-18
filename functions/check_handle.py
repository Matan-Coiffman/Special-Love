import os
import csv
import re

file_path = 'user_info.csv'


def check_or_create_csv():
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['first_name', 'age', 'password',
                             'phone_number', 'hobbies', 'interest'])
        print(f"File created: {file_path}")
    else:
        print(f"File exists: {file_path}")


def is_strong_password(password):
    if len(password) < 8:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    return has_letter and has_number


def check_age(age):
    try:
        age = int(age)
        return 18 <= age <= 120  # Reasonable age range
    except ValueError:
        return False


def check_string_name(name):
    return len(name) >= 2 and name.isalpha()


def check_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()


def add_user_info(full_name, age, password, phone_number):
    check_or_create_csv()

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([full_name, age, password, phone_number])
        print(f"User with phone number {phone_number} added successfully.")




