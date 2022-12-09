
from django import forms

class section(forms.Form):
    Title = forms.CharField()
    URL = forms.URLField()
    SMS = forms.CharField(widget=forms.Textarea)
    Press = forms.CharField(widget=forms.CheckboxInput)
    DontTouch = forms.ChoiceField(choices=((1, 'Why'), (2, 'What'), (3, 'Sleep')))