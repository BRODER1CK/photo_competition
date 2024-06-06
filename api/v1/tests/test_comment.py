from unittest import skip

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.test.client import encode_multipart
from rest_framework.test import APIClient

from models_app.factories.comment import CommentFactory
from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class CommentTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.photo = PhotoFactory(user=cls.user)
        cls.comment = CommentFactory(
            user=cls.user,
            content_type_id=ContentType.objects.get_for_model(
                apps.get_model("models_app", "Photo")
            ).id,
            object_id=cls.photo.id,
        )
        cls.nested_comment = CommentFactory(
            user=cls.user,
            content_type_id=ContentType.objects.get_for_model(
                apps.get_model("models_app", "Comment")
            ).id,
            object_id=cls.comment.id,
        )

    def test_view_list_for_photo_status_200(self):
        data = {
            "content_type": "Photo",
            "object_id": self.comment.object_id,
        }
        resp = self.client.get("/api/v1/comments/", data=data)
        self.assertEqual(resp.status_code, 200)

    def test_view_list_for_comment_status_200(self):
        data = {
            "content_type": "Comment",
            "object_id": self.comment.id,
        }
        resp = self.client.get("/api/v1/comments/", data=data)
        self.assertEqual(resp.status_code, 200)

    def test_view_show_status_200(self):
        data = {"id": self.comment.id}
        resp = self.client.get(f"/api/v1/comments/{self.comment.id}/", data=data)
        self.assertEqual(resp.status_code, 200)

    @skip("WIP")
    def test_view_create_for_photo_status_201(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "text": self.comment.text,
            "content_type": "Photo",
            "object_id": self.photo.id,
        }
        resp = self.client.post("/api/v1/comments/", data=data, headers=headers)
        self.assertEqual(resp.status_code, 201)

    @skip("WIP")
    def test_view_create_for_comment_status_201(self):
        headers = {
            "Authorization": f"{self.user.token}",
            "accept": "application/json",
        }
        data = {
            "user": self.user,
            "text": self.comment.text,
            "content_type": "Comment",
            "object_id": self.comment.id,
        }
        resp = self.client.post("/api/v1/comments/", data=data, headers=headers)
        self.assertEqual(resp.status_code, 201)

    def test_view_update_status_200(self):
        data = {"user": self.user, "text": self.comment.text, "id": self.comment.id}
        factory = APIClient()
        content = encode_multipart("BoUnDaRyStRiNg", data)
        content_type = "multipart/form-data; boundary=BoUnDaRyStRiNg"
        resp = factory.put(
            f"/api/v1/comments/{self.comment.id}/",
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
            "id": self.nested_comment.id,
        }
        resp = self.client.delete(
            f"/api/v1/comments/{self.nested_comment.id}/", data=data, headers=headers
        )
        self.assertEqual(resp.status_code, 200)
