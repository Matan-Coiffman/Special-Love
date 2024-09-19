import os
import csv

file_path = '../user_info.csv'


def check_or_create_csv():
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['first_name', 'age', 'password',
                             'phone_number', 'hobbies', 'interest'])
        print(f"File created: {file_path}")
    else:
        print(f"File exists: {file_path}")


def get_user_info_by_phone(phone_number):
    check_or_create_csv()

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['phone_number'] == phone_number:
                return row
    return None


def add_user_info(first_name, age, password, phone_number):
    check_or_create_csv()

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, age, password, phone_number])
        print(f"User with phone number {phone_number} added successfully.")
        
def get_users_dictionary():
    # read csv file to a list of dictionaries
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data
