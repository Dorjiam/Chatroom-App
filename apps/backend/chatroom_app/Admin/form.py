from django import forms

class send_messageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
