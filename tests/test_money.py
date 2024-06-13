from bank.money import Money


class TestMoney:
    def test_add(self):
        a = Money(10, 'USD', "$")
        b = Money(20, 'USD', "$")
        assert a + b == Money(30, 'USD', "$")

    def test_sub(self):
        a = Money(10, 'USD', "$")
        b = Money(20, 'USD', "$")
        assert a - b == Money(-10, 'USD', "$")

    def test_mul(self):
        a = Money(10, 'USD', "$")
        assert a * 11.1 == Money(111, 'USD', "$")

    def test_add2(self):
        a = Money(10, 'USD', "$","ja")
        assert a + 1 == Money(11, 'USD', "$")

    def test_compare(self):
        a = Money(10.98, 'USD', "$")
        if a >= 10:
            assert True
        else:
            assert False
