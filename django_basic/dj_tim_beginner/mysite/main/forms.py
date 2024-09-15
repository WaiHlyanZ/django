from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="List Name", max_length=200)
    check = forms.BooleanField(label="Done?", required=False)