from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin

from models_app.models.comment import Comment
from models_app.models.photo import Photo
from models_app.models.user import User

admin.site.register(User, UserAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ['title', 'status', 'description', 'get_current_photo', 'get_previous_photo', 'user']
    readonly_fields = ['get_current_photo', 'get_previous_photo']
    list_display = ['title', 'status', 'get_photo', 'user']
    list_display_links = ['title']
    list_editable = ('status', )
    ordering = ['-created_at', 'title']
    list_per_page = 5
    actions = ['set_published', 'set_awaits']
    search_fields = ['title']
    list_filter = ['status']
    save_on_top = True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status == 'P':
            return False
        return True

    @admin.display(description='Изображение', ordering='description')
    def get_photo(self, photo: Photo):
        if photo.current_photo:
            return mark_safe(f"<img src='{photo.current_photo.url}', width=100")
        else:
            return 'Без фото'

    @admin.display(description='Изображение', ordering='description')
    def get_current_photo(self, photo: Photo):
        if photo.current_photo:
            return mark_safe(f"<img src='{photo.current_photo.url}'")
        else:
            return 'Без фото'

    @admin.display(description='Предыдущее изображение', ordering='description')
    def get_previous_photo(self, photo: Photo):
        if photo.previous_photo:
            return mark_safe(f"<img src='{photo.previous_photo.url}'")
        else:
            return 'Без фото'

    @admin.action(description='Опубликовать выбранные Фотографии')
    def set_published(self, request, queryset):
        count = queryset.update(status='P')
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации выбранные Фотографии')
    def set_awaits(self, request, queryset):
        count = queryset.update(status='M')
        self.message_user(request, f'{count} записей снято с публикации', messages.WARNING)
