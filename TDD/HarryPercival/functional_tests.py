import unittest
import requests


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # Runs beffore tests
        self.session = requests.session()

    def tearDown(self):
        # Runs after tests, even if failure
        self.session.close()

    def test_success(self):
        url = "http://localhost:8091/"
        try:
            resp = self.session.get(url)
            self.assertTrue(resp.ok)
        except Exception as e:
            print(e)
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
