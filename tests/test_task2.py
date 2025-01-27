import unittest
import requests
import pytest

class Test_yandex_disk(unittest.TestCase):
    def setUp(self):
        self.headers = {
            'Authorization': 'token'
        }

    def test_create_folder2(self):
        for i, (param, folder_name, expected_code) in enumerate((

                ('path', 'pictures', 201),
                ('path', 'pictures', 409),
                ('pathhh', 'pictures', 400)
            )):

            with self.subTest(i): # номер теста
                params = {
                    param: folder_name
                }
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                    params = params,
                                    headers = self.headers)
                actual_code = response.status_code
                self.assertEqual(expected_code, actual_code)



