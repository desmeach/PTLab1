# -*- coding: utf-8 -*-
import argparse
import sys
import os
from QuartileRating import QuartileRating
from CalcRating import CalcRating
from JsonDataReader import JsonDataReader
from TextDataReader import TextDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    paths = get_path_from_arguments(sys.argv[1:])
    paths = paths.split(' ')
    for path in paths:
        filename, file_extension = os.path.splitext(path)
        if file_extension == '.json':
            json_reader = JsonDataReader()
            students = json_reader.read(path)
            print("Students: ", students)
            third_quartile_students = QuartileRating(students).calc()
            print("Third quartile students: ", third_quartile_students)
        elif file_extension == '.txt':
            reader = TextDataReader()
            students = reader.read(path)
            print("Students: ", students)
            rating = CalcRating(students).calc()
            print("Rating: ", rating)
        print('###################')


if __name__ == "__main__":
    main()
