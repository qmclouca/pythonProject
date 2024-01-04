import json
import random
from faker import Faker

# Initialize Faker
fake = Faker(['pt_BR'])

# Function to generate a random date of birth
def random_dob():
    return fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d%m%Y")

# Function to generate a random pedido
def generate_pedido():
    return {
        "numeroPedido": random.randint(1000000, 9999999),
        "tipoPedido": random.choice(["OBTDIGIT", "INVPDIGIT", "SRVDIGIT"]),
        "nomeIdent": fake.name(),
        "dataNasc": random_dob(),
        "numeroRG": None if random.choice([True, False]) else fake.rg(),
        "filiacao": [
            {"filiacao": fake.name() + " Pai"},
            {"filiacao": fake.name() + " Mãe"}
        ]
    }

# Generate 30 pedidos
pedidos = [generate_pedido() for _ in range(30)]

# Convert to JSON
json_data = json.dumps(pedidos, indent=4, ensure_ascii=False)

# Print the generated JSON
print(json_data)

# We'll save this to a file
path = '/mnt/data/pedidos.json'
with open(path, 'w', encoding='utf-8') as file:
    file.write(json_data)

path

