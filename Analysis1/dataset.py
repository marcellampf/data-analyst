# all my packages
# pip install faker
import pandas as pd
import random
import faker

# Start faker
fake = faker.Faker('en_US')

# Function to create my product
def random_product():
    products = ['Pants', 'T-shirt', 'Dress', 'Sneakers', 'Skirt', 'Hoodie', 'Jumpsuit', 'Blazer']
    return random.choice(products)

# Function to generate clients
def client_type():
    types = ['Regular', 'VIP', 'Premium', 'New']
    return random.choice(types)

data = []
for _ in range(200):
    data.append([
        fake.uuid4(),
        fake.name(),
        fake.date_of_birth(minimum_age=18, maximum_age=90),
        fake.first_name_male(),
        fake.first_name_female(),
        fake.street_address(),
        fake.city(),
        fake.state(),
        fake.zipcode(),
        fake.country(),
        fake.email(),
        fake.phone_number(),
        client_type(),
        fake.date_this_decade(),
        fake.date_time_this_year(),
        random_product(),
        random_product(),
        random_product(),
        random_product(),
        random_product(),
        round(random.uniform(100, 10000), 2),
        round(random.uniform(1000, 50000), 2),
        random.choice(['Ativa', 'Inativa', 'Suspensa']),
        random.choice(['Masculino', 'Feminino']),
        fake.job()
    ])

print("Data generation complete")

# Creating dataframe
columns = ['ID', 'Name', 'Date of Birth', 'Fathers Name', 'Mothers Name', 'Address', 'City', 'State', 'ZIP Code', 'Country', 'Email', 'Phone', 'Customer Type', 'Registration Date', 'Last Login', 'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Balance', 'Credit Limit', 'Account Status', 'Gender', 'Profession']
df = pd.DataFrame(data, columns=columns)

print("DataFrame creation complete")
print(df.head())

# Saving to a CSV file
# df.to_csv('clients_account.csv', index=False)
# print("Data saved to clients_account.csv")

print(df.head(10))  # Print the first 10 rows of the DataFrame