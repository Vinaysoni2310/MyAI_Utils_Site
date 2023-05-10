from django import forms
from .models import *

class UploadFileForm(forms.ModelForm):
    class Meta():
        model = BGRemover
        fields = '__all__'
        