import csv, os
class Database:
    def __init__(self):
        self.tables = {}
    def add_table(self, table_name, table):
        self.tables[table_name] = table
    def get_table(self, table_name):
        return self.tables.get(table_name)

class Table:
    def __init__(self, filename, database):
        self.filename = filename
        self.database = database
        self.data = self.read_csv()
    def read_csv(self):
        path = os.path.join(os.path.dirname(__file__), self.filename)
        with open(path, 'r') as file:
            return list(csv.DictReader(file))
    def insert(self, row):
        if isinstance(row, dict):
            self.data.append(row)
    def update(self, key, value, new_data):
        for row in self.data:
            if row[key] == value:
                row.update(new_data)
    def save(self):
        path = os.path.join(os.path.dirname(__file__), self.filename)
        with open(path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)


# ex test
if __name__ == '__main__':
    db = Database()
    persons_table = Table('persons.csv', db)
    db.add_table('persons', persons_table)
