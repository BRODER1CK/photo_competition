from django import forms

from models_app.models.photo import Photo


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'current_photo']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }