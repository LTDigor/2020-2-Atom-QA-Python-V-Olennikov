import pytest


class TestList:
    # приведение типов
    def test_list1(self):
        l = []
        assert bool(l) == False

    def test_list2(self):
        l = [1]
        assert bool(l) == True

    # длина списка
    @pytest.mark.parametrize('i', list(range(5)))
    def test_list3(self, i):
        l = [1] * i
        assert len(l) == i

    # сложение списков
    def test_list4(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l = l1 + l2
        assert l == [1, 2, 3, 4, 5, 6]

    # доступ по индексу
    @pytest.mark.parametrize('i', list(range(6)))
    def test_list5(self, i):
        l = [0, 1, 2, 3, 4, 5]
        assert l[i] == i
