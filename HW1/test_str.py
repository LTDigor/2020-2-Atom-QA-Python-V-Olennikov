import pytest


class TestStr:
    # приведение типов
    @pytest.mark.parametrize("s, expected", [('', False), ('1', True)])
    def test_str_type(self, s, expected):
        assert bool(s) == expected

    # длина строки
    @pytest.mark.parametrize('i', list(range(-1, 2)))
    def test_str_len(self, i):
        s = '1' * i
        if i > 0:
            assert len(s) == i
        else:
            assert len(s) == 0

    # сложение строк
    def test_str_sum(self):
        s1 = '1234'
        s2 = '5678'
        s = s1 + s2
        assert s == '12345678'

    # доступ по индексу
    def test_str_index(self):
        s = '1234'
        assert s[1] == '2'

    # выход индекса за пределы
    def test_str_index_error(self):
        s = '1234'
        with pytest.raises(IndexError):
            assert s[4] == '2'