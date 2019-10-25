from django import forms

class searchForm(forms.Form):
    post = forms.CharField(label='City', max_length=100, required=False)