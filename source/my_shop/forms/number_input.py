from django import forms

class NumberInputForm(forms.Form):
    count = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'style': 'width: 90px; height: 35px;',
    }))
