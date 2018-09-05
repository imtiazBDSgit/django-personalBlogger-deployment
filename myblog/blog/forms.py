from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,label='Name')
    email = forms.EmailField(required=True,label='Email Address')
    phone= forms.CharField(required=False,label='Phone Number')
    message = forms.CharField(widget=forms.Textarea, required=True,label='Message')
