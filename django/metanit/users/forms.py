from django import forms

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    password = forms.IntegerField()