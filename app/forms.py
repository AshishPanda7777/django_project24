from django import forms
from app.models import TOPIC, WEBPAGE, ACCESS_RECORD

class TOPICForm(forms.ModelForm):
    class Meta:
        model = TOPIC
        fields = '__all__'
        labels = {'topic_name': 'Topic Name'}

class WEBPAGEForm(forms.ModelForm):
    class Meta:
        model = WEBPAGE
        fields = '__all__'

class ACCESS_RECORDForm(forms.ModelForm):
    class Meta:
        model = ACCESS_RECORD
        fields = '__all__'
