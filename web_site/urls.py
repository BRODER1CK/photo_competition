from django.urls import path

from .views.add_photo import AddPhoto
from .views.delete_photo import DeletePhoto
from .views.index import Index
from .views.logout import Logout
from .views.restore_photo import RestorePhoto
from .views.show_photo import ShowPhoto
from .views.profile import Profile
from .views.edit_photo import EditPhoto


app_name = 'web_site'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('photo/<int:photo_id>/', ShowPhoto.as_view(), name='photo'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/add_photo/', AddPhoto.as_view(), name='add_photo'),
    path('profile/edit_photo/<int:photo_id>/', EditPhoto.as_view(), name='edit_photo'),
    path('profile/delete_photo/<int:photo_id>/', DeletePhoto.as_view(), name='delete_photo'),
    path('profile/restore_photo/<int:photo_id>/', RestorePhoto.as_view(), name='restore_photo'),
]
