from django import forms 
from myapp.models import MailModel


class MailForm(forms.ModelForm):
   
    class Meta:
        model = MailModel
        fields = '__all__'