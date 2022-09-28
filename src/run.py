import os
import sys
from script import save_to_csv, file


def convert_file(apkg_file):
    try:
        if os.path.exists(apkg_file):
            csv_file = f"{apkg_file}.csv".replace(".apkg", "")
            file(apkg_file)
            save_to_csv(csv_file)
        else:
            exit
    except Exception as e:
        print("File required")


if __name__ == "__main__":
    convert_file(sys.argv[1])
