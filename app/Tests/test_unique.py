from django.test import SimpleTestCase
# from rest_framework.test import APIClient

from myapp import views, calc


class ViewsTests(SimpleTestCase):

    def test_is_unique(self):
        """Test if value is unique"""
        res = views.is_unique('unique')
        self.assertEqual(res, 'unique')


class CalcTests(SimpleTestCase):

    def test_check_add(self):
        """Test the add function"""
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    def test_check_subtract(self):
        """Test the subtract function"""
        res = calc.subtract(6, 2)
        self.assertEqual(res, 4)


# class TestViews(SimpleTestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_get_greetings(self):
#         """Test getting greetings"""
#         res = self.client.get('/greetings/')

#         self.assertEqual(res.status_code, 200)
#         self.assertEqual(res.data, 'Hello, world!')
