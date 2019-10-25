from django import forms

class searchForm(forms.Form):
    your_name = forms.CharField(label='City', max_length=100)