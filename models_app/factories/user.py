import secrets

import factory

from models_app.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"Username {n}")
    email = factory.LazyAttribute(lambda n: f"{n.username}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    token = factory.Sequence(lambda _: secrets.token_hex(16))
