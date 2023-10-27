from django import forms

class StarsForm(forms.Form):
    rated_user = forms.CharField(required=True)
    stars = forms.IntegerField(required=True)

