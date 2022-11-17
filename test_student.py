import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # Must be camelCase to work
    def setUp(self):
        print('Ser Up')
        self.student = Student('John', 'Doe')

    # Must be camelCase to work
    def tearDown(self):
        print('Tear down')

    def test_full_name_method(self):
        print('full_name test')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        print('Naughty santa test')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('Test email')
        self.assertEqual(self.student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()
