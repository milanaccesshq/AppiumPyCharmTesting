from unittest import TestCase


class NinePlusTenRealPass(TestCase):
    def test_nine_plus_ten_real(self):
        from session.calculator_test_real import nine_plus_ten_real
        self.assertEqual(nine_plus_ten_real(), "19")


class SimpleCalculationReal(TestCase):
    def test_single_digit_calculation_real(self):
        from session.calculator_test_real import single_digit_calculation_real
        self.assertEqual(single_digit_calculation_real("9", "9", "mul"), "81")


class MultiCalculationReal(TestCase):
    def test_multi_digit_calculation_real(self):
        from session.calculator_test_real import multi_digit_calculation_real
        self.assertEqual(multi_digit_calculation_real("64", "16", "div"), "4")
