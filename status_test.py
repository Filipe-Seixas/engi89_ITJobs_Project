import unittest
import pytest
import requests
from check_status import StatusCheck


class StatusTest(unittest.TestCase):
    status = StatusCheck()

    def test_check_status_success(self):
        self.assertIs(self.status.check_status(200), 'Successful')

    def test_check_status_unsuccessful(self):
        self.assertIs(self.status.check_status(404), 'Unsuccessful')
