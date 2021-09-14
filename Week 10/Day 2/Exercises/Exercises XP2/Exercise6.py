from faker import Faker
fake = Faker()

users = []

def add_user():
    user = {}
    user['name'] = fake.name()
    user['address'] = fake.address()
    user['language code'] = fake.language_code()
    users.append(user)

add_user()
add_user()
add_user()
for user in users:
    print(user)