from django import forms


class NewStatus(forms.Form):
    text = forms.CharField(label='Name', max_length=200)
