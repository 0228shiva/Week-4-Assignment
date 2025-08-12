import pandas as pd
from src.booking_processor import process_reservations

def test_process_reservations(tmp_path):
    test_file = tmp_path / "test_res.csv"
    df = pd.DataFrame({
        "PNR": ["ABC123", "DEF456"],
        "Passenger": ["John Doe", ""],
        "Origin": ["JFK", "XXX"],
        "Destination": ["LAX", "LAX"],
        "Fare": [300, -10],
        "Status": ["CONFIRMED", "PENDING"]
    })
    df.to_csv(test_file, index=False)

    process_reservations(test_file)

    cleaned = pd.read_csv("data/cleaned_reservations.csv")
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["Passenger"] == "John Doe"
    assert cleaned.iloc[0]["Fare"] >= 0
