from django import forms


class PollForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    option_1 = forms.CharField(max_length=255, required=True)
    option_2 = forms.CharField(max_length=255, required=True)


class PollImgForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    image_1 = forms.ImageField()
    image_2 = forms.ImageField()
