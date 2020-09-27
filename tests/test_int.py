import pytest


class TestInt:
    # приведение типов
    def test_int1(self):
        b = 0
        assert bool(b) == False

    def test_int2(self):
        b = 1
        assert bool(b) == True

    # деление на 0
    @pytest.mark.parametrize('i', list(range(10)))
    def test_int3(self, i):
        with pytest.raises(ZeroDivisionError):
            assert i / 0

    # сложение
    def test_int4(self):
        b = 1
        c = 2
        a = b + c
        assert a == 3

    # умножение
    @pytest.mark.parametrize('i', list(range(3)))
    def test_int5(self, i):
        b = 10
        c = 5
        a = b * c
        assert a == 50

    # умножение на 0
    @pytest.mark.parametrize('i', list(range(10)))
    def test_int5(self, i):
        b = i
        assert b * 0 == 0
