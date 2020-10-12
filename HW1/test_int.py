import pytest


class TestInt:
    # приведение типов
    @pytest.mark.parametrize("d, expected", [(-1, True), (0, False), (1, True)])
    def test_int_type(self, d, expected):
        assert bool(d) == expected

    # деление на 0
    @pytest.mark.parametrize('i', list(range(-1, 2)))
    def test_int_div_zero(self, i):
        with pytest.raises(ZeroDivisionError):
            assert i / 0

    # сложение
    @pytest.mark.parametrize('a, i, expected', [(10, -1, 9), (10, 0, 10), (10, 1, 11)])
    def test_int_sum(self, a, i, expected):
        assert a + i == expected

    # умножение
    @pytest.mark.parametrize('a, i, expected', [(10, -1, -10), (1, 0, 0), (10, 1, 10), (-1, 0, 0), (0, 0, 0)])
    def test_int_mul(self, a, i, expected):
        assert a * i == expected

    # остаток от деления
    @pytest.mark.parametrize('a, i, expected', [(11, 1, 0), (11, 2, 1), (11, 11, 0), (11, 10, 1), (11, 12, 11)])
    def test_int_div_remainder(self, a, i, expected):
        if i == 0:
            with pytest.raises(ZeroDivisionError):
                assert a % i
        else:
            assert a % i == expected
