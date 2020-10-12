import pytest


class TestSet:
    # приведение типов
    @pytest.mark.parametrize("a, expected", [(set(), False), ({1}, True)])
    def test_set_type(self, a, expected):
        assert bool(a) == expected

    # длина множества
    @pytest.mark.parametrize('i', list(range(-1, 2)))
    def test_set_len(self, i):
        a = set(range(i))
        if i > 0:
            assert len(a) == i
        else:
            len(a) == 0

    # объединение множеств
    def test_set_union(self):
        a1 = {1, 2, 3}
        a2 = {4, 5, 6}
        a = set.union(a1, a2)
        assert a == {1, 2, 3, 4, 5, 6}

    # добавление существующего элемента
    def test_set_add(self):
        a = {1}
        a.add(1)
        assert a == {1}

    def test_set_intersection(self):
        a1 = {1, 2, 3, 4}
        a2 = {3, 4, 5, 6}
        a = a1 & a2
        assert a == {3, 4}
