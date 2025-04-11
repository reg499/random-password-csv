import csv
import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def create_password_csv(filename='passwords.csv', entry_count=10):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'url', 'username', 'password'])  # header row

        for i in range(1, entry_count + 1):
            site_name = f"Test Site {i}"
            url = f"https://example{i}.com"
            username = f"user{i}"
            password = generate_random_password()
            writer.writerow([site_name, url, username, password])

    print(f"{entry_count} passwords written to '{filename}'.")

create_password_csv()
