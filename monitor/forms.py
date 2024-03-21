from django import forms

class URLForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), label='Enter URL to monitor', required=True)

