import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    """
    Best test is, which can be run independently
    TDD: Test driven development means write tests before write the code.
    """
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp Func")
        self.empl_1 = Employee('Amir', 'Savvy', 50000)
        self.empl_2 = Employee('Amir', 'Engineer', 60000)

    def tearDown(self):
        print("tearDown Func")

    def test_full_name(self):
        print("test_full_name Func")
        self.assertEqual(self.empl_1.full_name, 'Amir Savvy')
        self.assertEqual(self.empl_2.full_name, 'Amir Engineer')

    def test_email(self):
        print("test_email Func")
        self.assertEqual(self.empl_1.email, 'amir.savvy@google.co')
        self.assertEqual(self.empl_2.email, 'amir.engineer@google.co')

    def test_apply_raise(self):
        print("test_apply_raise Func")
        self.empl_1.apply_raise()
        self.empl_2.apply_raise()

        self.assertEqual(self.empl_1.pay, 52500)
        self.assertEqual(self.empl_2.pay, 63000)

    def test_monthly_schedule(self):
        print("test_monthly_schedule Func")

        with patch('employee.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = 'Success'

            schedule = self.empl_1.monthly_schedule('July')
            mock_get.assert_called_with('http://google.co/Savvy/July')
            self.assertEqual(schedule, 'Success')

            mock_get.return_value.ok = False

            schedule = self.empl_2.monthly_schedule('June')
            mock_get.assert_called_with('http://google.co/Engineer/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()