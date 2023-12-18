import csv, os

class Database:
    def __init__(self):
        self.tables = {}

    def add_table(self, table_name, table):
        self.tables[table_name] = table

    def get_table(self, table_name):
        return self.tables.get(table_name)

    def save_all(self):
        for table in self.tables.values():
            table.save()

class Table:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_csv()

    def read_csv(self):
        data = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        return data

    def insert(self, row):
        self.data.append(row)

    def update(self, key, value, new_data):
        for row in self.data:
            if row[key] == value:
                row.update(new_data)

    def save(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)
