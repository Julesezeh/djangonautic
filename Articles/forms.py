from tkinter import Widget
from django import forms
from .models import Articles

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','slug','body','thumbnail']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'My New Article'}),
            'slug':forms.TextInput(attrs={'placeholder':'my-new-article'}),
            'body':forms.Textarea(attrs={'placeholder':'Once upon a time in .......'})

        }

class EditArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','slug','body','thumbnail']
        