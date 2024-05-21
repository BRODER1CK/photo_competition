import factory

from models_app.factories.user import UserFactory
from models_app.models.photo import Photo


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: f"Photo {n}")
    description = factory.Faker("text")
    current_photo = factory.django.FileField(
        filename="test.png", data=open("media/web_site/default.png", "rb").read()
    )
