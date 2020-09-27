import pytest


class TestSet:
    # приведение типов
    def test_set1(self):
        a = set()
        assert bool(a) == False

    def test_set2(self):
        a = {1}
        assert bool(a) == True

    # длина множества
    @pytest.mark.parametrize('i', list(range(5)))
    def test_set3(self, i):
        a = set(range(i))
        assert len(a) == i

    # объединение множеств
    def test_set4(self):
        a1 = {1, 2, 3}
        a2 = {4, 5, 6}
        a = set.union(a1, a2)
        assert a == {1, 2, 3, 4, 5, 6}

    # добавление существующего элемента
    def test_set5(self):
        a = {1}
        a.add(1)
        assert a == {1}
