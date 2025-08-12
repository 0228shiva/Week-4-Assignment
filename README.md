Week 4 – Flight Reservation Debug Lab

Overview:
This project simulates a basic flight reservation system. It includes tools to generate synthetic flight reservation data and process it through a booking processor. This lab is designed to teach debugging and automation skills by fixing broken code and improving data handling pipelines.

Project Structure:
.
├── README.txt
├── generate_sample_data.py → Script to generate synthetic flight reservations
├── main.py → Main script to process the reservation data
├── requirements.txt → List of required Python packages
├── data/
│ └── reservations.csv → Generated flight reservations (output)
└── src/
└── booking_processor.py → Contains the logic to validate and process reservation records

Setup Instructions:

Clone or Download the Project:
Download or extract the Week4-FlightDebugLab folder to your local machine.

Create and Activate a Virtual Environment:
Open a terminal (PowerShell recommended) and navigate to the project directory.

python -m venv .venv

For PowerShell (after fixing execution policy if needed):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
..venv\Scripts\Activate.ps1

For CMD:
..venv\Scripts\activate.bat

Install Required Packages:
pip install -r requirements.txt

Generate Sample Data:
Run the following to create a CSV of fake reservations:

python generate_sample_data.py 200

This will create a file called data/reservations.csv with 200 rows.

Run the Main Script:
python main.py

This script will:

Load the generated reservation data

Clean and validate records

Output a filtered dataset and logs

Troubleshooting:

If you get a “sdf is not defined” error, open src/booking_processor.py and correct the typo: change sdf to df.

Make sure your virtual environment is activated before installing or running anything.

If script activation fails due to PowerShell execution policy, use:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Author:
Week 4 – FlightDebugLab Team
Course: Applied Programming & Automation
