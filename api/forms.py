from django import forms
from ckeditor.widgets import CKEditorWidget

class UsernameForm(forms.Form):
    body = forms.CharField(widget=CKEditorWidget())

class PasswordForm(forms.Form):
    body = forms.CharField(widget=CKEditorWidget())
