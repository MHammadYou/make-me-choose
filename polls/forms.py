from django import forms


class PollForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    option_1 = forms.CharField(max_length=255, required=True)
    option_2 = forms.CharField(max_length=255, required=True)
