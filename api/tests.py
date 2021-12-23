from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class URLTestCases(APITestCase):
    def test_create_url(self):
        client = APIClient()
        data = {"url": "https://google.com/"}
        response = client.post("/_short", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_custom_url(self):
        client = APIClient()
        host = "http://testserver/"
        shorten = "aaaAaa"
        data = {"url": "https://google.com/", "shorten": shorten}
        response = client.post("/_short", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["shorten"], host + shorten)

    def test_create_existing_url(self):
        client = APIClient()
        shorten = "aaaAaa"
        data = {"url": "https://google.com/", "shorten": shorten}
        client.post("/_short", data)
        response = client.post("/_short", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_redirect_url(self):
        client = APIClient()
        data = {"url": "https://google.com/"}
        response_create = client.post("/_short", data)
        response = client.get(response_create.data["shorten"])
        self.assertRedirects(
            response, data["url"], status_code=302, target_status_code=200
        )
