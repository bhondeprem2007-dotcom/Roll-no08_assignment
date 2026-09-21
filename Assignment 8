import csv
import json

def read_csv(file_name):
    with open(file_name, "r", newline="") as file:
        data = csv.DictReader(file)
        return list(data)

def write_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def convert_csv_to_json(csv_file, json_file):
    data = read_csv(csv_file)
    write_json(json_file, data)
    return data

if __name__ == "__main__":

    csv_file = "students.csv"
    json_file = "students.json"

    data = (
        "id,name,department,marks\n"
        "1,Aditi,Computer Science,88\n"
        "2,Rahul,Mechanical,76\n"
        "3,Sneha,Electronics,92\n"
    )

    with open(csv_file, "w", newline="") as file:
        file.write(data)

    print("CSV file created successfully!")
    print("\nCSV Data:")

    with open(csv_file, "r") as file:
        print(file.read())

    result = convert_csv_to_json(csv_file, json_file)

    print("CSV converted to JSON successfully!")
    print("Number of records:", len(result))

    print("\nJSON Data:")

    with open(json_file, "r") as file:
        print(file.read())
