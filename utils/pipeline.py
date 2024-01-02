def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None

    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

    if url:
        user.avatar = url
        user.save()
        print(user.avatar)
