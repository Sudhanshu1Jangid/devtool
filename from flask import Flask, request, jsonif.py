import base64
import json
import csv
import yaml
from datetime import datetime

def csv_to_json(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_data = json.dumps([row for row in csv_reader], indent=4)
        return json_data

def base64_encode(data):
    encoded_data = base64.b64encode(data.encode()).decode()
    return encoded_data

def base64_decode(data):
    decoded_data = base64.b64decode(data.encode()).decode()
    return decoded_data

def json_formatter(data):
    formatted_json = json.dumps(json.loads(data), indent=4)
    return formatted_json

def yaml_to_json(data):
    json_data = json.dumps(yaml.safe_load(data), indent=4)
    return json_data

def timestamp_to_date(timestamp):
    date = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    return date

if __name__ == '__main__':
    while True:
        print("\nUtility App")
        print("1. CSV to JSON")
        print("2. Base64 Encode")
        print("3. Base64 Decode")
        print("4. JSON Formatter")
        print("5. YAML to JSON")
        print("6. Timestamp to Date")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            csv_file_path = input("Enter CSV file path: ")
            print(csv_to_json(csv_file_path))
        elif choice == '2':
            data = input("Enter data to encode: ")
            print(base64_encode(data))
        elif choice == '3':
            data = input("Enter data to decode: ")
            print(base64_decode(data))
        elif choice == '4':
            data = input("Enter JSON data: ")
            print(json_formatter(data))
        elif choice == '5':
            data = input("Enter YAML data: ")
            print(yaml_to_json(data))
        elif choice == '6':
            timestamp = input("Enter timestamp: ")
            print(timestamp_to_date(timestamp))
        elif choice == '7':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
