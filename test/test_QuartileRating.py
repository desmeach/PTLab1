# -*- coding: utf-8 -*-
from src.Types import DataType
from src.QuartileRating import QuartileRating
import pytest
RatingsType = dict[str, float]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, list]:
        data: DataType = {
            "Иванов Иван Иванович":
                [
                    ("математика", 67),
                    ("литература", 100),
                    ("программирование", 91)
                ],
            "Петров Петр Петрович":
                [
                    ("математика", 78),
                    ("химия", 87),
                    ("социология", 61)
                ],
            "Иванов Петр Дмитриевич":
                [
                    ("математика", 71),
                    ("литература", 61),
                    ("программирование", 61)
                ],
            "Антонов Антон Денисович":
                [
                    ("социология", 61),
                    ("химия", 83),
                    ("философия", 61)
                ],
            "Пупкин Демид Романович":
                [
                    ("математика", 86),
                    ("история", 92),
                    ("химия", 100)
                ],
            "Добров Иван Александрович":
                [
                    ("программирование", 78),
                    ("математика", 87),
                    ("социология", 61)
                ]
        }
        students: list = ['Иванов Иван Иванович',
                          'Петров Петр Петрович',
                          'Пупкин Демид Романович',
                          'Добров Иван Александрович'
                          ]
        return data, students

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      list]) -> None:
        calc_rating = QuartileRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType,
                                          list]) -> None:
        students = QuartileRating(input_data[0]).calc()
        assert students == input_data[1]
