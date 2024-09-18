import os
import csv

file_path = 'user_info.csv'


def check_or_create_csv():
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # phone number = user id
            writer.writerow(
                    ['first_name', 'sec_name', 'password', 'phone_number',
                     'hobbies'])
        print(f"File created: {file_path}")
    else:
        print(f"File exists: {file_path}")

    return open(file_path, mode='r')


def get_user_info_by_phone(phone_number):
    # Check if file exists, if not create it
    check_or_create_csv()

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['phone_number'] == phone_number:
                print(row['phone_number'])
                return row  # Return the row as a dictionary
    return None  # Return None if no matching phone number was found


def add_user_info(first_name, sec_name, password, phone_number, hobbies):
    check_or_create_csv()  # Make sure the file exists before writing to it

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, sec_name, password, phone_number, hobbies])
        print(f"User with phone number {phone_number} added successfully.")