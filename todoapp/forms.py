from . models import Task
from django import forms




class ToDO(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']
