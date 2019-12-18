"""
@ Description
    Brief example how to handle csv files

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        files_example.py
"""
import xml.etree.ElementTree as ET
import csv


class FilesHandler:
    def __init__(self):
        print("Object built successfully ")

    def csv_open_files(self, file_path):
        file = open(file_path, 'r+')
        reader = csv.reader(file)
        data = list(reader)
        self.get_status_csv(data=data)
        writer = csv.writer(file, delimiter=',', lineterminator='\n')

        for row in range(1, 4):
            print(row)
            data[row+1][4] = "passed"
        for line in data:
            print(line)
            writer.writerow(line)

        self.get_status_csv(data=data)
        file.close()

    def csv_with_files(self, file_path):
        with open(file_path, 'r+') as file:
            reader = csv.reader(file)
            data = list(reader)
            self.get_status_csv(data=data)
            writer = csv.writer(file, delimiter=',', lineterminator='\n')

            for row in range(1, 4):
                print(row)
                data[row + 1][4] = "passed"
            for line in data:
                print(line)
                writer.writerow(line)

            self.get_status_csv(data=data)

    @staticmethod
    def get_status_csv(data):
        for n in range(len(data)-2):
            print("Test name: %s  Status: %s" % (data[n+1][1], data[n+1][4]))


file_path = "path_file"
with open(file_path, 'r+') as file:
    reader = csv.reader(file)

file = open("welcome.txt")
data = file.read()
print(data)
file.close()

with open("welcome.txt") as file:
   data = file.read()

# region yaml parser
import yaml
with open("yamo.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print("Error on YAML file")
# endregion yaml parser


# region opt parser
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-o', action="store", default="default value")
    options, args = parser.parse_args()
    print(options.o)

"""
D:\Trainings\Repo\Python\parsers>opt_oct.py
default value
D:\Trainings\Repo\Python\parsers>opt_oct.py -o "different value"
different value
"""
# endregion opt parser


# region xml parser

tree = ET.parse('document.xml')
root = tree.getroot()

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
# endregion xml parser


if __name__ == "__main__":
    test = FilesHandler()
    file_path = r"your_file_location"
    test.csv_open_files(file_path=file_path)
    test.csv_with_files(file_path=file_path)
