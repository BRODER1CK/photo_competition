from django.urls import path

from .views.add_photo import AddPhoto
from .views.index import Index
from .views.logout import Logout
from .views.show_photo import ShowPhoto
from .views.profile import Profile
from .views.edit_photo import EditPhoto


app_name = 'web_site'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('photo/<int:id>/', ShowPhoto.as_view(), name='photo'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('add_photo/', AddPhoto.as_view(), name='add_photo'),
    path('edit_photo/<int:id>/', EditPhoto.as_view(), name='edit_photo'),
]
