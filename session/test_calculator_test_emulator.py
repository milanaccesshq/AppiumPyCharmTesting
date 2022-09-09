from unittest import TestCase


class NinePlusTenPass(TestCase):
    def test_nine_plus_ten(self):
        from session.calculator_test_emulator import nine_plus_ten
        self.assertEqual(nine_plus_ten(), "19")


# class NinePlusTenFail(TestCase):
#     def test_nine_plus_ten(self):
#         from session.calculator_test import nine_plus_ten
#         self.assertEqual(nine_plus_ten(), "21")


class SimpleCalculation(TestCase):
    def test_single_digit_calculation(self):
        from session.calculator_test_emulator import single_digit_calculation
        self.assertEqual(single_digit_calculation("2", "3", "mul"), "6")


class MultiCalculation(TestCase):
    def test_multi_digit_calculation(self):
        from session.calculator_test_emulator import multi_digit_calculation
        self.assertEqual(multi_digit_calculation("200", "1000", "add"), "1200")
        self.assertEqual(multi_digit_calculation("33", "11", "sub"), "22")
        self.assertEqual(multi_digit_calculation("12", "12", "mul"), "144")
        self.assertEqual(multi_digit_calculation("45", "9", "div"), "5")

