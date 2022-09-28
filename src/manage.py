from genericpath import isdir
import os
import sys
from script import save_to_csv, file
from run import convert_file


def convert_directory(directory):
    for name in os.scandir(directory):
        if name.is_file() and name.path.endswith(".apkg"):
            convert_file(name.path)
        elif not name.is_file():
            convert_directory(name.path)


if __name__ == "__main__":
    try:
        if os.path.isdir(sys.argv[1]):
            convert_directory(sys.argv[1])
        else:
            exit
    except Exception as e:
        print("Directory path does not exist")
