from django import forms


from .models import Topic


from ckeditor.widgets import CKEditorWidget



class CreateTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('wsyg',)

        widgets = {
            
            'wsyg': forms.CharField(widget=CKEditorWidget()),
        }

      
