from django import forms

class DateForm(forms.Form):
    study_date = forms.DateField(label='Study Date:')
