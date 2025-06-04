# main.py
# This script creates a CSV file with student data

import csv

# Sample student data: [Name, Age, Math Score, English Score]
rows = [
    ["Name", "Age", "Math", "English"],
    ["Ali", 17, 88, 75],
    ["Sara", 16, 92, 81],
    ["Omar", 18, 79, 90],
]

# Write to CSV file
with open("students.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file 'students.csv' created successfully.")
