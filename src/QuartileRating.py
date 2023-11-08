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
        quartile_value = percentile([0, 100], 25 * quartile_idx)
        for student in students_avg_ratings:
            if students_avg_ratings[student] >= quartile_value:
                self.students.append(student)
        return self.students

    # 1 1 2 _3 4 7 7 7 _8 8 8 8 9 _9 9 9 9 9
    # i*(n+1/4)
    # 1*(19/4) = 4.75
    # 2*(19/4) = 9.5
    # 3*(19/4) = 14.25
    # 1 1 2 3
    # 4 7 7 7 8
    # 8 8 8 8 9
    # 9 9 9 9 9
