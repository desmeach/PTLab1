# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader


class TestJsonDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = ("{\"Иванов Иван Александрович\": "
                "{\"математика\": 67,"
                "\"литература\": 90,"
                "\"биология\": 70 "
                "},"
                "\"Петров Дмитрий Иванович\": "
                "{\"русский\": 78,"
                "\"иностранный язык\": 87"
                "}"
                "}")
        data = {
            "Иванов Иван Александрович": [
                ("математика", 67),
                ("литература", 90),
                ("биология", 70)
            ],
            "Петров Дмитрий Иванович": [
                ("русский язык", 78),
                ("иностранный язык", 87)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content:
                          tuple[str, DataType], tmpdir) \
            -> tuple[str, DataType]:

        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
