"""
@ Description
    Brief example how to handle csv files

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        files_example.py
"""
import csv


class FilesHandler:
    def __init__(self):
        print "Object built successfully "

    def csv_open_files(self, file_path):
        file = open(file_path, 'r+')
        reader = csv.reader(file)
        data = list(reader)
        self.get_status_csv(data=data)

        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        for row in range(1, 4):
            print row
            data[row+1][4] = "passed"

        for line in data:
            print line
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
                print row
                data[row + 1][4] = "passed"
            for line in data:
                print line
                writer.writerow(line)

            self.get_status_csv(data=data)

    def get_status_csv(self, data):
        for n in range(len(data)-2):
            print "Test name: %s  Status: %s" % (data[n+1][1], data[n+1][4])


if __name__ == "__main__":
    test = FilesHandler()
    file_path = r"your_file_location"
    test.csv_open_files(file_path=file_path)
    test.csv_with_files(file_path=file_path)
