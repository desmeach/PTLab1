# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating
import pytest
RatingsType = dict[str, float]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
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
        rating_scores: RatingsType = {
            "Иванов Иван Иванович": 86.0000,
            "Петров Петр Петрович": 75.3333,
            "Иванов Петр Дмитриевич": 64.3333,
            "Антонов Антон Денисович": 68.3333,
            "Пупкин Демид Романович": 92.6666,
            "Добров Иван Александрович": 75.3333,
        }
        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType,
                                          RatingsType]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
