
from django import forms

class SubscribeFrom(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    matn_email=forms.CharField(max_length=1000)
