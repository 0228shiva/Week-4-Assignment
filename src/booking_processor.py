import pandas as pd
import logging
from src.utils import validate_airport_code

logging.basicConfig(level=logging.INFO)

def process_reservations(file_path):
    df = pd.read_csv(file_path)
    logging.info(f"Loaded {len(df)} reservations")

    # Clean and validates
    df["Passenger"] = df["Passenger"].fillna("UNKNOWN")
    df["Passenger"] = df["Passenger"].replace("", "UNKNOWN")
    df = df[df["Fare"] >= 0]
    df = df[df["Origin"].apply(validate_airport_code)]
    df = df[df["Destination"].apply(validate_airport_code)]
    df.drop_duplicates(subset=["PNR"], inplace=True)

    logging.info(f"Cleaned data has {len(df)} valid reservations")
    df.to_csv("data/cleaned_reservations.csv", index=False)
