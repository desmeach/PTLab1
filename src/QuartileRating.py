# -*- coding: utf-8 -*-
from Types import DataType
from CalcRating import CalcRating
from numpy import percentile


class QuartileRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.students: list = []

    def calc(self, quartile_idx=3) -> list:
        students_avg_ratings = CalcRating(self.data).calc()
        print(list(students_avg_ratings.values()))
        quartile_value = percentile([0, 100], 25 * quartile_idx)
        for student in students_avg_ratings:
            if students_avg_ratings[student] >= quartile_value:
                self.students.append(student)
        return self.students
