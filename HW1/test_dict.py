import pytest


class TestDict:
    # приведение типов
    @pytest.mark.parametrize("d, expected", [({}, False), ({'1': 1}, True)])
    def test_dict_type(self, d, expected):
        assert bool(d) == expected

    # доступ по ключу для существующего элемента
    def test_dict_access_pos(self):
        d = {2: 4}
        assert d[2] == 4

    # доступ по ключу для несуществующего элемента
    def test_dict_access_neg(self):
        d = {'2': 4}
        with pytest.raises(KeyError):
            assert d[2] == 4

    # очищение словаря
    def test_dict_clear(self):
        d = {1: 1}
        d.clear()
        assert not d

    # обновление словаря имеющимся ключом
    def test_dict_values(self):
        d = {1: 1, '2': 2, (1, 2): 3}
        d[1] = 4
        assert d[1] == 4
