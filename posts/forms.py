from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()

class CommentForm(forms.Form):
    message = forms.CharField()