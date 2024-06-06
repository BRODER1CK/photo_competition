from django.test import TestCase

from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class LikeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.photo = PhotoFactory(user=cls.user)

    def test_view_list_status_200(self):
        data = {
            "photo_id": self.photo.id,
        }
        resp = self.client.get("/api/v1/likes/", data=data)
        self.assertEqual(resp.status_code, 200)

    def test_view_create_status_200(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "photo_id": self.photo.id,
        }
        resp = self.client.post(
            f"/api/v1/likes/{self.photo.id}/", data=data, headers=headers
        )
        self.assertEqual(resp.status_code, 200)

    def test_view_delete_status_200(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "photo_id": self.photo.id,
        }
        resp = self.client.delete(
            f"/api/v1/likes/{self.photo.id}/", data=data, headers=headers
        )
        self.assertEqual(resp.status_code, 200)
