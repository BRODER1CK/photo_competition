from api.v1.views.comment import ListCommentView, UpdateDeleteCommentView
from api.v1.views.like import CreateDeleteLikeView, ListLikeView
from api.v1.views.photo import RetrieveUpdateDeletePhotoView, ListPhotoView, CreatePhotoView

from django.urls import path

from api.v1.views.user import RetrieveUpdateUserView

urlpatterns = [
    path('photo/', ListPhotoView.as_view()),
    path('photo/<int:id>/', RetrieveUpdateDeletePhotoView.as_view()),
    path('photo/create/', CreatePhotoView.as_view()),
    path('photo/<int:id>/like/', CreateDeleteLikeView.as_view()),
    path('photo/<int:id>/likes/', ListLikeView.as_view()),
    path('photo/<int:id>/comments/', ListCommentView.as_view()),
    # path('photo/<int:id>/comments/<int:id>/', UpdateDeleteCommentView.as_view()),
    path('profile/', RetrieveUpdateUserView.as_view()),
]
