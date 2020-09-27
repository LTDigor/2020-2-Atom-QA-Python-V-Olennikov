import pytest


class TestDict:
    # приведение типов
    def test_dict1(self):
        d = {}
        assert bool(d) == False

    def test_dict2(self):
        d = {'1': 1}
        assert bool(d) == True

    # доступ по ключу
    def test_dict3(self):
        d = {1: 2, 2: 4, 3: 9}
        assert d[2] == 4

    # доступ по ключу для несуществующего элемента
    def test_dict4(self):
        d = {'2': 4}
        with pytest.raises(KeyError):
            assert d[2] == 4

    # добавление элемента
    @pytest.mark.parametrize('i', list(range(3)))
    def test_dict5(self, i):
        d = {i: 'i'}
        assert d[i] == 'i'
