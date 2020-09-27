import pytest


class TestStr:
    # приведение типов
    def test_str1(self):
        s = ''
        assert bool(s) == False

    def test_str2(self):
        s = '1'
        assert bool(s) == True

    # длина строки
    @pytest.mark.parametrize('i', list(range(5)))
    def test_str3(self, i):
        s = '1' * i
        assert len(s) == i

    # сложение строк
    def test_str4(self):
        s1 = '1234'
        s2 = '5678'
        s = s1 + s2
        assert s == '12345678'

    # доступ по индексу
    def test_str5(self):
        s = '1234'
        assert s[1] == '2'
