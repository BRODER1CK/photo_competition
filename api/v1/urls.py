from django.urls import path

from api.v1.views.comment import ListCreateCommentView, UpdateDeleteCommentView
from api.v1.views.like import CreateDeleteLikeView, ListLikeView
from api.v1.views.photo import ListCreatePhotoView, RetrieveUpdateDeletePhotoView
from api.v1.views.user import GenerateTokenView, RetrieveUpdateUserView

urlpatterns = [
    path("photos/", ListCreatePhotoView.as_view()),
    path("photos/<int:id>/", RetrieveUpdateDeletePhotoView.as_view()),
    path("likes/", ListLikeView.as_view()),
    path("likes/<int:photo_id>/", CreateDeleteLikeView.as_view()),
    path("comments/", ListCreateCommentView.as_view()),
    path("comments/<int:id>/", UpdateDeleteCommentView.as_view()),
    path("profile/", RetrieveUpdateUserView.as_view()),
    path("profile/generate_token/", GenerateTokenView.as_view()),
]
