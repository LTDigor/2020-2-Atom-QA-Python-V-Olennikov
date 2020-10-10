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
    @pytest.mark.parametrize('a, i, expected', [(10, -1, -10), (10, 0, 0), (10, 1, 50)])
    def test_int_mul(self, a, i, expected):
        assert a + i == expected

    # умножение на 0
    @pytest.mark.parametrize('i', list(range(-1, 2)))
    def test_int_mul_zero(self, i):
        assert i * 0 == 0
