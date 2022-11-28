import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 3) == 15

    def test_multiply_calculate_correctly(self):
        assert self.calc.division(self, 20, 4) == 5

    def test_multiply_calculate_correctly(self):
        assert self.calc.subtraction(self, 100, 30) == 70

    def test_multiply_calculate_correctly(self):
        assert self.calc.adding(self, 30, 45) == 75




