from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-o', action="store", default="default value")
    options, args = parser.parse_args()
    print options.o
"""
D:\Trainings\Repo\Python\parsers>opt_oct.py
default value
D:\Trainings\Repo\Python\parsers>opt_oct.py -o "different value"
different value
"""