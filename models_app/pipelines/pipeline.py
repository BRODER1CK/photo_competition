def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None

    if backend.name == "vk-oauth2":
        url = response.get("photo", "")

    if url:
        user.avatar = url
        user.save()


def get_email(backend, response, user=None, *args, **kwargs):
    url = None

    if backend.name == "vk-oauth2":
        url = response.get("email", "")

    if url:
        user.email = url
        user.save()
