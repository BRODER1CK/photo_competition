import factory

from models_app.factories.user import UserFactory
from models_app.models.photo import Comment


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    text = factory.Faker("text")
