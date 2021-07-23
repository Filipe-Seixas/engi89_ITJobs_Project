from app import flask_app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = flask_app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_table_page_loads_title(self):
        tester = flask_app.test_client(self)
        response = tester.get('/job/AWS', content_type='html/text')
        self.assertTrue(b'AWS' in response.data)
        response = tester.get('/job/DevOps', content_type='html/text')
        self.assertTrue(b'DevOps' in response.data)

    def test_table_page_loads_table_headers(self):
        tester = flask_app.test_client(self)
        response = tester.get('/job/AWS', content_type='html/text')
        self.assertTrue(b'Date' in response.data)
        self.assertTrue(b'Rank' in response.data)
        self.assertTrue(b'Median Salary' in response.data)
        self.assertTrue(b'Historical Permanent Job ads' in response.data)
        self.assertTrue(b'Live Jobs' in response.data)
