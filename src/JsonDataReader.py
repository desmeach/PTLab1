# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str):
        with open(path, encoding='utf-8') as file:
            templates = json.load(file)
            for student, subjects in templates.items():
                if student:
                    self.key = student
                    self.students[self.key] = []
                if subjects:
                    for subj, score in subjects.items():
                        self.students[self.key].append(
                            (subj.strip(), score)
                        )
            return self.students
