from django import forms


class NameForm(forms.Form):
   userId = forms.CharField(max_length=20)
   # file