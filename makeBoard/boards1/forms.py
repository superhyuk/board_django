from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from ckeditor.fields import RichTextField
 
class RichForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = (
            'content',
        )
 

