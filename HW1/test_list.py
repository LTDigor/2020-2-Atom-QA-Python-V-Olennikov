import pytest


class TestList:
    # приведение типов
    @pytest.mark.parametrize("li, expected", [([], False), ([1], True)])
    def test_list_type(self, li, expected):
        assert bool(li) == expected

    # длина списка
    @pytest.mark.parametrize('i', list(range(2)))
    def test_list_len(self, i):
        li = [1] * i
        if i >= 0:
            assert len(li) == i

    # сложение списков
    def test_list_sum(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        res = l1 + l2
        assert res == [1, 2, 3, 4, 5, 6]

    # доступ по индексу
    @pytest.mark.parametrize('i', list(range(0, 2)))
    def test_list_access(self, i):
        li = [0, 1]
        assert li[i] == i

    # выход за пределы списка
    @pytest.mark.parametrize('i', [2, -3])
    def test_list_access_neg(self, i):
        li = [0, 1]
        with pytest.raises(IndexError):
            assert li[i]
