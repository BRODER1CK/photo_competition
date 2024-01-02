from api.v1.views.photo import RetrieveUpdateDeletePhotoView, ListPhotoView, CreatePhotoView

from django.urls import path

from api.v1.views.user import RetrieveUpdateUserView

urlpatterns = [
    path('photo/', ListPhotoView.as_view()),
    path('photo/<int:id>/', RetrieveUpdateDeletePhotoView.as_view()),
    path('photo/create/', CreatePhotoView.as_view()),
    path('profile/', RetrieveUpdateUserView.as_view()),
]
