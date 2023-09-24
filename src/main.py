# -*- coding: utf-8 -*-
import argparse
import sys
from QuartileRating import QuartileRating
from JsonDataReader import JsonDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    json_reader = JsonDataReader()
    students = json_reader.read(path)
    print("Students: ", students)
    third_quartile_students = QuartileRating(students).calc()
    print("Third quartile students: ", third_quartile_students)


if __name__ == "__main__":
    main()
