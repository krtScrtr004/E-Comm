import csv

# Utility Class for CSV Operations
class CSVHandler:
    @staticmethod
    def read_csv(file_path):
        try:
            with open(file_path, 'r') as file:
                return list(csv.DictReader(file)) # Return data as list
        except FileNotFoundError:
            return []

    @staticmethod
    def write_csv(file_path, data, fieldnames):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            