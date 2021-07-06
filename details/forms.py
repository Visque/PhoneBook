from django import forms

class SampleForm(forms.Form):
    samplefield = forms.BooleanField(initial=True, required=True)