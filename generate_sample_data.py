import csv
import random
from faker import Faker

fake = Faker()

def generate_data(num=200):
    airports = ["JFK", "LAX", "ORD", "DFW", "DEN", "ATL", "SFO", "SEA"]
    statuses = ["CONFIRMED", "CANCELLED", "PENDING"]
    
    with open("data/reservations.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["PNR", "Passenger", "Origin", "Destination", "Fare", "Status"])
        writer.writeheader()
        for _ in range(num):
            writer.writerow({
                "PNR": fake.unique.bothify(text='???###'),
                "Passenger": fake.name() if random.random() > 0.05 else "",  # 5% blank names
                "Origin": random.choice(airports),
                "Destination": random.choice(airports),
                "Fare": round(random.uniform(-50, 1000), 2),  # Can include negative fares
                "Status": random.choice(statuses)
            })

if __name__ == "__main__":
    generate_data(200)
