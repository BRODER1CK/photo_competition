from django.test import TestCase
from django.test.client import encode_multipart
from rest_framework.test import APIClient

from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class PhotoTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.photo = PhotoFactory(user=cls.user)

    def test_view_list_status_200(self):
        resp = self.client.get("/api/v1/photos/")
        self.assertEqual(resp.status_code, 200)

    def test_view_show_status_200(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        resp = self.client.get(f"/api/v1/photos/{self.photo.id}/", headers=headers)
        self.assertEqual(resp.status_code, 200)

    def test_view_create_with_max_parameters_status_201(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "title": self.photo.title,
            "description": self.photo.description,
            "current_photo": self.photo.current_photo,
        }
        resp = self.client.post("/api/v1/photos/", data=data, headers=headers)
        self.assertEqual(resp.status_code, 201)

    def test_view_create_without_any_parameters_status_400(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "current_photo": self.photo.current_photo,
        }
        resp = self.client.post("/api/v1/photos/", data=data, headers=headers)
        self.assertEqual(resp.status_code, 400)

    def test_view_create_without_parameters_status_400(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
        }
        resp = self.client.post("/api/v1/photos/", data=data, headers=headers)
        self.assertEqual(resp.status_code, 400)

    def test_view_update_with_max_parameters_status_200(self):
        data = {
            "user": self.user,
            "title": self.photo.title,
            "description": self.photo.description,
        }
        with open("media/web_site/default.png", "rb") as self.test_photo:
            data["current_photo"] = self.test_photo
            factory = APIClient()
            content = encode_multipart("BoUnDaRyStRiNg", data)
            content_type = "multipart/form-data; boundary=BoUnDaRyStRiNg"
            resp = factory.put(
                f"/api/v1/photos/{self.photo.id}/",
                content,
                content_type=content_type,
                HTTP_AUTHORIZATION=f"{self.user.token}",
            )
            self.assertEqual(resp.status_code, 200)

    def test_view_update_with_any_parameters_status_200(self):
        data = {
            "user": self.user,
        }
        with open("media/web_site/default.png", "rb") as self.test_photo:
            data["current_photo"] = self.test_photo
            factory = APIClient()
            content = encode_multipart("BoUnDaRyStRiNg", data)
            content_type = "multipart/form-data; boundary=BoUnDaRyStRiNg"
            resp = factory.patch(
                f"/api/v1/photos/{self.photo.id}/",
                content,
                content_type=content_type,
                HTTP_AUTHORIZATION=f"{self.user.token}",
            )
            self.assertEqual(resp.status_code, 200)

    def test_view_update_without_parameters_status_200(self):
        data = {
            "user": self.user,
        }
        factory = APIClient()
        content = encode_multipart("BoUnDaRyStRiNg", data)
        content_type = "multipart/form-data; boundary=BoUnDaRyStRiNg"
        resp = factory.patch(
            f"/api/v1/photos/{self.photo.id}/",
            content,
            content_type=content_type,
            HTTP_AUTHORIZATION=f"{self.user.token}",
        )
        self.assertEqual(resp.status_code, 200)

    def test_view_delete_status_200(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "id": self.photo.id,
        }
        resp = self.client.delete(
            f"/api/v1/photos/{self.photo.id}/", data=data, headers=headers
        )
        self.assertEqual(resp.status_code, 200)
