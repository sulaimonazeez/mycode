from .models import musicUploader
from django import forms

class adminManage(forms.ModelForm):
  class Meta:
    model = musicUploader
    fields = '__all__'