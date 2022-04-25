from django import forms
from .models import Topic

from django_summernote.fields import SummernoteTextFormField


class SummerForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = (
            'content',
        )