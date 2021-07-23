from app import flask_app
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = flask_app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
